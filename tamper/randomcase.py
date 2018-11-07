import random


__PRIORITY__ = 9


def tamper(script):
    retval = []
    for c in script:
        do_replace = random.randint(1, 2) == 1
        if do_replace:
            c = c.upper()
        retval.append(c)
    return ''.join(retval)