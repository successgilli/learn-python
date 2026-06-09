## Mines 💣
- Values for default parameters/arguments are evaluated at definition time and not runtime.
- Actual parameters are not copied but passed as reference to formal parameters, so care should be taken since the input could be modified
- As a result of the above, it is advisable that mutable types are not used as default params. Or if they are needed, use a default of `None` with a check to initialize at runtime.
Notice how the input `a` is modified from within the func.

```py
def good(val: int, input: list = []):
    input.append(val)

a = [0]

good(2, a) # a = [0, 2]
good(4, a) # a = [0, 2, 4]
good(7, a) # a = [0, 2, 4, 7]

print(a) # a = [0, 2, 4, 7]
```
- Lambda arguments are not evaluated at definition time.
They are evaluated at runtime with the scope.

Below, without the default param `x`, calling f,g and h would greet same `Dave` since it will be the latest value in scope for the lambda. This leverages default param behaviour described above that is evaluated at definition time and bound to the functions `__defaults__` magic value.

```py
from typing import Callable

names  = ['Ben', 'Rita', 'Dave']

def  getGreetingFunctions(names: list[str]) -> list[Callable[[str], None]]:
    funcs = []

    for name in names:
        funcs.append(lambda x=name:print(f'Hello {x}'))
    
    return funcs

f, g, h = getGreetingFunctions(names)

f()
g()
h()
```
- Lambdas bind variables not values. Basically, they implement closures by default with the current scope.
When a lambda is called, the variable(s) value is the latest at execution time.
- For more predictable anonymous function behaviour, use `functools.partial`

```py
from functools import partial
def do(a,b, c):
    return a*b*c

runPart = partial(do, 4,3,5)

print(runPart())

```
