import math


def handle_zero_division(fn):
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except ZeroDivisionError:
            return math.inf
    return wrapped
