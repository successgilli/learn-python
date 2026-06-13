## Generators

A generator expression is an object that carries out same computation as a list comprehension but produces the results iteratively.

This allows for some space management by **not** creating the list in memory but on demand like the `range` function.

Only difference is that instead of square brackets, they use parenthesis. Also, operations of a list do not apply to the generator object created although the generator can still be converted to a list if needed.

```py
with open('./study-notes/basic.md') as file:
    items = (i for i in file.readlines() if i.startswith('#'))

    for i in items:
        print(i)
```

- `next` can be used to get the next value in the generator sequence and will throw an error on reaching the end.
- Generator values can only be used once. After each return, we exhaust the values in the generator until it is empty.

### Generators and yield
If a function uses the `yield` keyword, it defines a generator.

Generator functions can simply be written as below using the `yield` keyword

```py
def gen():
    for i in [3,4,5]:
        yield i

for i in gen():
    print(i)
```

### Restarting generators
Generators work by exhausting their items. However, they can be restarted or repeated if you want by implementing an `__iter__` magic method like so.
```py
class CountIt:
    def __init__(self, items):
        self.items = items
    
    def __iter__(self):
        for item in self.items:
            yield item

countIt = CountIt([4,6])

for i in countIt:
    print(i)

for i in countIt:
    print(i)

next(countIt.__iter__())
```
### Generator delegation
Generators are usually driven from the outside and cannot run on its own but instead returns a generator object and as such, implementing packages that allows to run generator functions might become difficult to interact with. For this reason, we have `yield from`. This delegates the iteration to an outer layer.

E.G Below, we have a `greet` generator that is used inside a `callGreet` function.
The example shows how `yield from` delegates the iteration of the `greet` generator to `callGreet`.

```py
def greet():
    yield 2

def callGreet():
    yield greet()

for i in callGreet():
    print(i)
```
Without `from`, `callGreet` would simply return a generator object.

### Enhanced generators or Generator coroutines
This involves the usage of generators as receivers instead of producers.
Here, the generator appears on the right side of statements

```py
...
n = yield
```

With this statement, you can send items to the generator and it will store it inside n and continue running the generator till it hits `yield` again.

```py
def receiver():
    print('starting receiver')

    while True:
        print('waiting for next')
        n = yield
        print(f'{n} received')

r = receiver()

print('before None')
r.send(None) # Start the generator
r.send(1)
r.send(2)
r.send(5)
r.close() # Close the generator; errors on subsequent 'send' attempts.
```
output
```txt
before None
starting receiver
waiting for next
1 received
waiting for next
2 received
waiting for next
5 received
waiting for next
```