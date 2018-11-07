import random


__PRIORITY__ = 8


def tamper(script):
    retval = ""
    for c in script:
        do_it = random.randint(1, 3) == 1
        if do_it:
            if c == "(":
                c = "(("
            elif c == ")":
                c = "))"
        retval += c
    return retval