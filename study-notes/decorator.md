## Decorators
A decorator is a function that wraps around another function. Its primary aim is to enhance or modify the behavior of the wrapping object.

```py
@decorator
def func():
    ...
```
This is similar to

```py
def func():
    ...

func = decorator(func)
```

### Sample trace decorator implementation

```py
from typing import Callable

def trace(func: Callable):
    def call(*args, **kwargs):
        print(f'Calling function {func.__name__} with args: {args}, and kwargs {kwargs}')
        func(*args, **kwargs)

    return call

@trace
def add(x,y):
    print(x+y)

add(2,3)

# Output
# ----
# Calling function add with args: (2, 3), and kwargs {}
# 5
# ----
```

### Decorators need to ensure and preserve metadata
Function/objects carry meta data.

When we decorate them, we want to ensure that meta data detail is not lost and we can do that
using the `wraps` decorator from `functools` like so:

```py
from typing import Callable
from functools import wraps

def trace1(func: Callable):
    def wrapper():
        return func()
    
    return wrapper

def trace2(func: Callable):
    @wraps(func)
    def wrapper():
        return func()
    
    return wrapper


@trace1
def hello1():
    print('hi')

@trace2
def hello2():
    print('hi')

print(hello1.__name__) # wrapper
print(hello2.__name__)  # hello2
```
### Sample decorator with args implementation
```py
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
```
