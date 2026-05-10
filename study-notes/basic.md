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
print('{0} + {1} = {2}'.format(x, y, x + y))
print(f'{x} + {y} = {x+y}')
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

### Text Strings
The following are valid string literals
```py
a = 'Hello World'
b = "Python is groovy"
c = '''Computer says no.'''
d = """Computer still says no."""
```

- Strings are a sequence of unicode characters with index starting at zero (0).
- Over the wire and for storage, utf-8 encoding is the default for strings.
- Negative indexing works and starts from the end of the string. EG `'1234'[-1]` `== '4'`
- To extract sub strings, you can use slices/slicing with s[i:j] where `j` is not included.

**Common string methods:**
- `join`: returns a string separated by supplied separator from a list.
```py
','.join(['e','r','4']) # 'e,r,4'
```
- `split`: splits a string into a list and requires a non empty string argument else raises an exception. with a non-empty argument, it returns a list with items based on supplied argument used for the split.

```py
'1,2,3'.split() # ['1,2,3']
'1,2,3'.split(',') # ['1','2','3']

# TO create a list for each item in a string to simulate splitting by an empty string do the below
list('abc') # ['a','b','c']
```
- `lower`: converts a string to lower case
- `upper`: converts a string to upper case
- `replace`: replace a substring with count param to signify occurrence to replace
- `strip`: removes leading and trailing white spaces or characters supplied in args
- `startswith` and `endswith`: checks if string starts and ends with substring.

### File Input and Output
Files can be read with the `open` directive.
```py
file = open('./study-notes/basic.md')

text = file.read()

print(text)

file.close()
```
`with` directive can be used for better resource management. This ensures the resource is automatically closed and freed outside the `with` block.

```py
with open('./study-notes/basic.md') as file:
    for line in file:
        print(line)

# Sample to read chunks
with open('./study-notes/basic.md') as file:
    while (chunk := file.read(1000)):
        print(chunk)
```
You can also open files in a specific mode.
If file is not opened in a mode that supports your operation, you end up with an error. E.G Opening a file in read mode and then trying to write to that file. In the example below, you see how we open a file in `w` mode and then write to it.

```py
with open('./study-notes/basic.md') as file:
    with open('./study-notes/out.md', 'w') as outfile:
        while (chunk := file.read(1000)):
            outfile.write(chunk)
            # Or call print with file param
            print(chunk, file=outfile)
```
Inputs can be read from the terminal with the blow.
```py
text = input('put something here: ')
```

## Lists
