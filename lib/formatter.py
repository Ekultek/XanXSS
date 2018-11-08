import time


def debug(string):
    """
    output a dark blue debug string
    """
    timer = time.strftime("%H:%M:%S")
    print("\033[36m[debug]\033[0m[{}] {}".format(timer, string))


def info(string):
    """
    output a light green information string
    """
    timer = time.strftime("%H:%M:%S")
    print("\033[1m\033[92m[info][{}]\033[0m {}".format(timer, string))


def warning(string):
    """
    output a dark yellow warning string
    """
    timer = time.strftime("%H:%M:%S")
    print("\033[33m[warning][{}]\033[0m {}".format(timer, string))


def error(string):
    """
    output a red error string
    """
    timer = time.strftime("%H:%M:%S")
    print("\033[91m[error][{}]\033[0m {}".format(timer, string))
