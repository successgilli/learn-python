from functools import wraps
from typing import Callable

def trace_decorator_with_msg(msg=''):
    def wrapper(func: Callable):
        @wraps(func)
        def funcArgs(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)

        return funcArgs

    return wrapper

@trace_decorator_with_msg('labalala')
def addItem(a,b):
    return a + b

print(addItem(2,4), addItem.__name__)
