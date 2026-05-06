## Python Basics

### Basic python types
```py
print(type(3))
print(type("".join(reversed(['1','f']))))
print(type(3.0))
print(type(True))
```

```sh
# Output
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
```

- In python, everything is an object.
- Type hinting is just there for third party tools and improved maintenance and readability but it is ignored by the interpreter. Other types can still be assigned that violates the typing used.
```py
x:int = 2
x = "ab"
print(x) # ab
```


### String formatting
We can use the f-string for properly formatting strings like so
```py
# a and b are variables
x = f'{a} is same as {b}'
```
We can also leverage directive in the f-string to format the output further with indentation, decimal approximation, etc.
```py
# a and b are int variables
x = f'{a:>3d} is same as {b:0.2f}'
```

see [Datacamp's string formatting tutorial](https://www.datacamp.com/tutorial/python-f-string?utm_cid=23781701478&utm_aid=196565213035&utm_campaign=260417_1-ps-dscia~amx-tofu~python_2-b2c_3-emea_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=1010481-&utm_mtd=p-c&utm_kw=python%20string%20format&utm_source=google&utm_medium=paid_search&utm_content=ps-dscia~emea-en~amx~tofu~tutorial~python&gad_source=1&gad_campaignid=23781701478&gbraid=0AAAAADQ9WsEViSxBnkcsMRr1eMI8PKTzf&gclid=CjwKCAjwqubPBhBOEiwAzgZX2uKS8g3gN1aAZcamivhpcDDxc3xTarekYdEmM9QLZpHK-uvztY9HihoCE6sQAvD_BwE)

### Arithmetic Operation

```py
x = 3
y = 10

# Addition
print(x + y)

# Subtraction
print(x - y)

# Multiplication
print(x * y)

# Power: X raised to the power y === pow(x, y)
print(x ** y)

# Division
print(y / x)

# Integer division truncation
print(y // x) 

# Integer division truncation
print(y % x)
```

### Comparison Operators
- Greater than: `>`
- Less than: `<`
- Equal to: `==`
- Not equal to: `!=`
- Greater than or equal to: `>=`
- Less than or equal: `<=`

### Logical Operators
- This or That: `x or y`
- This and that: `x and y`
- Not this: `not x`

### No `++` and `--`
Other languages do have these but not in python.

To do similar just do

```py
x += 1 # same as x = x + 1
x *= 2

# This can be done with any of the arithmetic operators
```

### Conditionals and Control flow
```py
if condition:
    pass # do something
elif condition:
    pass # do something else
else:
    pass # conclude
```

You can also do inline conditional assignment:
```py
val = 3 if x == 1 else 4
```
Also possible to use dynamic assignment with walrus in while loops like so.
```py
while (y := x * 3) > 1:
    print(y, " here")
    x -= 1
```
Else conditions after/used with loops signals a statement to run after loop exists naturally
```py

while (y := x * 3) > 1:
    print(y, " here")
    x -= 1
    # break # A break, error or return in a loop will cause `else` to not run
else:
    print("done")

for x in range(10):
    print(x)
    # break # A break, error or return in a loop will cause `else` to not run
else:
    print("done 2")
```
