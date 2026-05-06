'''
Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

Solution
- Since both arrays are already sorted, we can easily combine them with a loop
- we will start at the first index of each, compare, then push the smaller into a new array.
- The idex we did push will be moved forward
- The index that was not pushed will remain untouched.
- Doing this means, one will be exhausted at some point.
- A condition to guide that both indices are still valid during the iteration
- If during the loop any index is exhausted, we exit.
- This means only one of them is left, a while loop guarded by if index < length should be applied on both arrays and allow looping to add the remaining elements.
'''
def combineSorted(arr1: list[int], arr2: list[int]) -> list[int]:
    indexArr1, indexArr2 = 0,0
    result = []

    while indexArr2 < len(arr2) and indexArr1 < len(arr1):
        arr1Item = arr1[indexArr1]
        arr2Item = arr2[indexArr2]

        if arr1Item < arr2Item:
            result.append(arr1Item)
            indexArr1 += 1
        else:
            result.append(arr2Item)
            indexArr2 += 1
    

    while indexArr1 < len(arr1):
        result.append(arr1[indexArr1])
        indexArr1 += 1

    while indexArr2 < len(arr2):
        result.append(arr2[indexArr2])
        indexArr2 += 1

    
    return result


print(combineSorted([2,3,6,20], [1,3,9,10]))
