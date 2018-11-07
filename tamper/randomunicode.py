import string
import random


__PRIORITY__ = 10


def tamper(script):
    acceptable_characters = string.hexdigits
    lowercase = string.ascii_lowercase
    retval = []
    for c in script:
        do_it = random.randint(0, len(script)) in range(len(retval) - 2, len(retval))
        if do_it:
            if c in acceptable_characters:
                c = "{}\u00{}{}".format(c, random.randint(1, 9), random.choice(lowercase))
        retval.append(c)
    return ''.join(retval)
