import math


def handle_zero_division(fn):
    """
    Wraps division function that throws ZeroDivisionError
    Passes up math.inf instead as a sensible response
    :param fn:
    :return:
    """
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except ZeroDivisionError:
            return math.inf
    return wrapped
