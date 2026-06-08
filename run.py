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
