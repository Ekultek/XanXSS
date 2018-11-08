import string
import random


__PRIORITY__ = 10


def tamper(script):
    acceptable_characters = string.hexdigits
    retval = []
    for c in script:
        do_it = random.randint(0, len(script)) in range(len(retval) - 2, len(retval))
        if do_it:
            if c in acceptable_characters:
                c = "%%u%.4X" % random.randrange(0x10000)
        retval.append(c)
    return ''.join(retval)
