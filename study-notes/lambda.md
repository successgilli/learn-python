## Lambda
These allows us to create small anonymous functions with the expression.

```txt
resp = lambda <args>: <expression/result>
```

```py
z = lambda x,y : x + y

x = 2
y = 1

z(x,y) # 3 
```

As callback func

```py
def do_something(val: int, func=lambda input : input*2):
    print(func(val))

do_something(20) # 40
```

### Currying
Function currying is a functional programming concept where a multi-argument function is expressed as a chain of nested functions instead. This was named in honour of the logician called Haskell Curry.

```py
def func(x,y,z)-> int:
    return x * y * z

def CurriedFunc(arg):
    return lambda arg1: lambda arg2: arg * arg1 * arg2

print(func(1,3,5), CurriedFunc(1)(3)(5))
```
