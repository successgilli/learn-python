## Named tuple

Sometimes we intend to return multiple return values and as such, we reach for a tuple.

```py
def func() -> tuple[int, int]:
    cost = 20
    totalCount = 2

    return [cost, totalCount]
```

Notice how difficult it is to know exactly what is where in the return type.

You may have to peak into the function or read func docs if any.

A better solution would be a named tuple; allowing us to access results by name without guessing positions while preserving the behavior of tuples if needed.

```py
from typing import NamedTuple


class MyReturnTuple(NamedTuple):
    cost: int
    
    totalCount: int

def func() -> MyReturnTuple:
    cost = 20
    totalCount = 2

    return MyReturnTuple(cost=cost, totalCount=totalCount)

resp = func()

print(resp.cost, resp.totalCount)
```
