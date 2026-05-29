## Context manager
This is a resource management tool that automatically allocates and releases resources when you need them.

An example is with the file opener.

```py
with open('file.md') as file:
    ...
```
The `with` directive associated with resource managers allow for an automatic management of resources when we enter and leave scope.

### Custom manager
A custom manager can be built to manage resources in a same way.

The manager class must satisfy the basics of a resource manager:
- it is a class
- An `__enter__` method that allocates/initializes the resource. Return self
- An `__exit__` method that deallocates resources. Accepts 3 params.
    -   type: Type of error
    -   value: the exception value
    -   traceback: the traceback associated with the exception 
- If no exceptions where raised during the resource usage at exist time, all 3 params will be None. If there was, then these values will be associated with the Exception.
- The exit method returns a boolean. False means we propagate errors which is the default if they happen and True means we don't.

```py
class MyManager():
    '''
    My manager haha
    '''
    def __init__(self, startCount: int):
        self.startCount = startCount
        self.items = [startCount]
    
    def __enter__(self):
        print('entering')
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        print('exiting')
        print(self.items)
        return True # Decides if errors are propagated should they happen during resource usage
    
    def do(self, item):
        print(f'doing {item}')
        self.items.append(item)

items = [284,4,2,5,3]

with MyManager(3) as resource:
    for item in items:
        resource.do(item)
    
    raise Exception('bla')

# entering
# doing 284
# doing 4
# doing 2
# doing 5
# doing 3
# exiting
# [3, 284, 4, 2, 5, 3]
```
