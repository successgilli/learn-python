## Prefix sum
This is a technique that allows us to find the sum of sub arrays in constant time.

It involves building a prefix array where each item in this new array corresponds with the sum at i in the original array.

E.G given nums = [5, 2, 1, 6, 3, 8], the prefix sum array would be `[5, 7, 8, 14, 17, 25]`.

Now:
- The sum up to an index is simply `prefix[index]`
- The sum between any two index is `prefix[j] - prefix[i-1]` or `prefix[j]-prefix[i] + originalArray[i]`

```py
def prefixSum(nums: list[int])->list[int]:
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[i-1])
    
    return prefix

print(prefixSum([5, 2, 1, 6, 3, 8]))
```

### Sample problem
Sample problem: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].

```py
def validQueries(nums: list[int], queries: list[tuple[int, int]], limit: int)->list[bool]:
    queryCheck = []
    prefix = [nums[0]]

    # Build prefix
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[i-1])
    
    for indices in queries:
        summation = prefix[indices[1]] - prefix[indices[0]] + nums[indices[0]]

        print(summation, limit)
        queryCheck.append(summation < limit)
    
    return queryCheck


print(validQueries([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13))
# ans -> [True, False, True]
```
