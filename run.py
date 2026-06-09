from functools import wraps
from typing import Callable

def trace_decorator_with_msg(msg='default message: '):
    def decorate(func: Callable):
        @wraps(func)
        def call(*args, **kwargs):
            print(f'{msg} calling function {func.__name__}')
            return func(*args, **kwargs)

        return call

    return decorate

@trace_decorator_with_msg('Running decorator')
def add(x,y):
    return x+y

print(add(2, 4))
