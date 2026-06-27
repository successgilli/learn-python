```py
# Sample code showing some patterns with async ctx usage and class tooling.

import asyncio
from abc import ABC, abstractmethod

class mySbs(ABC):
    @abstractmethod
    def do(self):
        pass

class MyAsyncCtx(mySbs):
    list_item = 90

    def __int__(self):
        return self

    async def __aenter__(self):
        print('entering')
        self.list_items = []

        return self
    
    def do(self):
        self.list_items.append(23)
        print('doing something')
        self.check()
        MyAsyncCtx.checkClass()
    
    async def __aexit__(self, exc_type, exc, tb):
        print('exiting')
    
    @classmethod
    def checkClass(cls):
        print(f'check class {cls.list_item}')
    
    @staticmethod
    def check():
        print('checking')
    
    @property
    def items(self):
        return self.list_items
    
    @items.setter
    def items(self, val):
        self.list_items.append(val)
    



async def main():
    async with MyAsyncCtx() as ctx:
        ctx.do()
        print(ctx.items, ' these are them')
        ctx.items = 78
        print(ctx.items)

asyncio.run(main())
```
