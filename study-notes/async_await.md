## Async-Await
Python supports asynchronous programming via async/await directives.

Asynchronous functions are functions that allow programs to be executed asynchronously and are called `coroutines` or `awaitables`.

```py
import asyncio

async def greet(msg='hello'):
    print(msg)


asyncio.run(greet())

async def main(msg):
    await greet(msg)

asyncio.run(main('hello from main'))
```

### Async and Sync combination
Python does not allow for async implementations to run with sync implementations and mixing them can be a complex topic.

As such, most times, support is provided for handling async behavior built separately.

Example is with the context manager below providing support for async implementation.

```py
import asyncio


class MyAsyncCtx:
    items: list[int]

    def __init__(self, items: list[int]):
        self.items = items
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        print(f'exiting... with final {self.items}')
    
    async def do(self, item: int):
        print('doing something')
        self.items.append(item)

async def main():
    async with MyAsyncCtx([3,4]) as ctx:
        await ctx.do(40)

asyncio.run(main())
```
