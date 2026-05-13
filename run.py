

def prefixSum(nums: list[int])->list[int]:
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[i-1])
    
    return prefix

print(prefixSum([5, 2, 1, 6, 3, 8]))


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
