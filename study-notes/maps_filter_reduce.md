## Maps, Filters and Reduce
- Python provides a built-in `maps` function to create a map from an iterable. These basically act as generators
- Python provides a built-in `filter` function to create a filter for an iterable. These basically act as generators
- We also have reduce from `functools`

```py
from functools import reduce

items = [1,3,4,5]

print(items)

# -- Maps ---
def mapItem(item):
    return item**item

print('--- Maps ---')
mappedItems = map(mapItem, items)

for i in mappedItems:
    print(i)

# -- Filter ---
print('--- Filter ---')
filteredItems = filter(lambda x: x**x > 100, items)

for i in filteredItems:
    print(i)

# -- Reduce ---
print('-- Reduce to an object ---')

def redItem(result: dict, item: int) -> dict:
    result[item] = item**item
    return result

reducedItems = reduce(redItem, items, {})

print(reducedItems)

# --- OUTPUT ---
#
# [1, 3, 4, 5]
# --- Maps ---
# 1
# 27
# 256
# 3125
# --- Filter ---
# 4
# 5
# -- Reduce to an object ---
# {1: 1, 3: 27, 4: 256, 5: 3125}
```
