import random


__PRIORITY__ = 3


def tamper(script):
    retval = []
    fillers = ("/*/", "/+/", "//", "&#13;", "%00", "`", "&#160;")
    for c in script:
        if c == " ":
            c = random.choice(fillers)
        retval.append(c)
    return ''.join(retval)
