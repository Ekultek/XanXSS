import re
import random


__PRIORITY__ = 2


def tamper(script):
    retval = []
    filler = ('%09', '%0a', '%0d', '+', "&#34;&#62;", "&#160;")
    searcher = re.compile("=")
    for c in script:
        if searcher.search(c) is not None:
            c = "={}".format(random.choice(filler))
        retval.append(c)
    return ''.join(retval)
