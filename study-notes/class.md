## Classes

### Using weak ref example with instance cache
Python provides a way to observe objects in memory without allowing them own memory.

For instance, if you want a cache to automatically remove items instead of a manual process to remove items, you could use a weak reference.

That way, the reference count does not increase and immediately the original item is garbage collected, the weak reference becomes dead.

This can be implemented with the `weakRef` module

```py
import weakref

class B:
    value = 6

b = B()
print(b.value)

bref = weakref.ref(b)
del b
print(bref())
```
From the above, `bref` can still reference `b` but allows `b` to be garbage collected and at which point returns `None` moving forward since the reference is gone.

This can be immediately used with caching where `weakref` module provisions like `WeakValueDictionary` allows you to manage dictionary references automatically giving out of the box clean up with such data structures.

Below, we explore the `weakref` module that allows us to hold reference to an object without increasing their reference count and as such, pointing to them until they are garbage collected. This mechanism is illustrated below allowing us to clear a cache automatically simply by implementing `WeakValueDictionary` from the weakrefd module removing items from a cache automatically as they are no longer needed while allowing access to them while available.

Without the weakref implementation, cache would grow unless we manually implement a clean up method.

```py
import weakref

class Date:
    _cache = weakref.WeakValueDictionary()

    # Bypass init to hook into instance creation
    def __new__(cls,year, month, day):
        instance = Date._cache.get((year, month, day))

        if not instance:
            self = object.__new__(cls)
            self.year = year
            self.month = month
            self.day = day
    
            Date._cache[(year, month, day)] = self
            return self
        else:
            return instance

    def __init__(self, *_):
        pass

a = Date(2000,29,9)
b = Date(2000,29,10)
print(list(Date._cache.keys()))
del b
print(list(Date._cache.keys()))

# Output
# [(2000, 29, 9), (2000, 29, 10)]
# [(2000, 29, 9)]
```
### Delegation
Inheritance is one way to allow object call or inherit from other classes.
However, there is another technique called `delegation`.

Here, you could leverage the `__getattr__` magic method to instead call methods from a different class not defined in the current class.
E.G:
```py
class A:
    def cry(self):
        print('😭')
    
    def shout(self):
        print('🤯')
    
    def greet(self):
        print('Hello')

class B:
    def __init__(self):
        self._a = A()
    
    def greet(self):
        print('Hello from B')
    
    def __getattr__(self, name):
        return self._a.__getattribute__(name)

b = B()

b.greet()
b.shout()
b.cry()
# Hello from B
# 🤯
# 😭
```

### Slots
Every time an instance is created, a new namespace is associated with it in its `__dict__` attribute. This can cause a significant amount of memory used if instances of this class are used in considerable numbers.

To combat this, you can use `slots` allowing us define a more compact structure to only hold what the instance needs as it concerns attributes thus, saving us space.
FYI: Slots do not support multiple inheritance.

```py
import sys

class A:
    __slots__ = ('name', 'title')
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def cry(self):
        print('😭')
    
    def shout(self):
        print('🤯')
    
    def greet(self):
        print('Hello')

class B:
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def cry(self):
        print('😭')
    
    def shout(self):
        print('🤯')
    
    def greet(self):
        print('Hello')
    
a = A('Ben', 'Benito')
b = B('Ben', 'Benito')
print(A.__dict__)
print(B.__dict__)
print(f'Size of instance a is {sys.getsizeof(A)} bytes')
print(f'Size of instance b is {sys.getsizeof(B)} bytes')
```
