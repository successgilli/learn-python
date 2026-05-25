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
