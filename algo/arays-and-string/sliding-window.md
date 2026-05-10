## Sliding window
This algorithm works for solutions requiring matching sub arrays on a constraint for `less than` or `greater than`.

For working with sub arrays, you may need to run `O(n**2)` to touch all sub arrays for a one dimensional array and to have to compare against constraint `k`. This is the brute force for solving sub arrays.

With sliding window, if the sub array solution fits the mental model, you can solve this question in `O(2n) == O(n)` since we will only go through the entire list at most once.

### Mental model
- We initialize two pointers at the start
- We move right (expand window)
- we check for validity
- we move left (shrink window) to maintain a valid window.
- Items in the window after each iteration corresponds to new sub arrays that match our constraint.
- Problem must be such that constraint is monotonic with the sub arrays. Meaning, shrinking must guarantee validity or invalidity based on the problem. E.G for numbers, if the items in array can be negative, then we cannot guarantee that shrinking for a sum constraint can guarantee validity or invalidity.
Because based on signum, a truncated/shrinked-out value could validate the sub array in combination with a future value. Hence such problems do not fit the sliding window.
If shrinking the window is not guaranteed to move sub arrays consistently and reliably towards validity or invalidity, then this algorithm cannot be used as it breaks down.

### Technique - at most
This pattern is the most common.

The idea is to get all contiguous sub arrays that are at most up to or equal to a constraint say `k`.

- Initialize pointers at the start of the array 
- expand right
- check for invalidity based on constraint
- if window becomes invalid, shrink window in a loop till window becomes valid again.
- collect sub arrays
- repeat till right reaches the end of the array

The idea is to expand the window till `at most` constraint is broken. if broken, shrink till it becomes valid again.

```
for right in inputItems {
    collect item at position right

    while constraint is broken for collected items and left <= right {
        remove item at position left (shrink)
        left++
    }

    collect answer/sub arrays.
    sub arrays = right -left + 1 or length of collected items.
}
```

### Technique - at least
This pattern is the least common.

The idea is to get all contiguous sub arrays that are greater than or equal to a constraint say `k`.

- Initialize pointers at the start of the array 
- expand right
- if valid, then collect answer, if not valid, move ahead to expand right
- if after expanding right, the result becomes valid, now, at the point we can start collecting answers.
- open a loop that when valid will continue shrinking the window. The loop starts by first recording the new sub arrays/answer, then shrinks the window

The idea is to expand the window till `at least` constraint is valid. if valid, shrink and collect answers till it becomes invalid again.

```
for right in inputItems {
    collect item at position right

    while constraint is valid for collected items and left <= right {
        collect answer/sub arrays.
        sub arrays = right -left + 1 or length of collected items.

        remove item at position left (shrink)
        left++
    }
}
```

### Technique - exact match
Some algorithms require that the constraint is an exact match.

These cannot be solved with the classic methods highlighted above because validity is a single point not a range, so there's no safe direction to move. Every move risks jumping over valid state with no way back.

To solve exactness we can apply a two sliding windows.

```
exact = atMost(k) - atMost(k-1)
```

If we get all sub arrays that are at most a value and then get all that are at most 1 less than that value, then the subtraction gives us the sub arrays left that are exactly value.

`atMost(5) - atMost(4) = items equal to 5`.

At most 5 includes subarrays with sum 0, 1, 2, 3, 4, and 5.
At most 4 includes subarrays with sum 0, 1, 2, 3, and 4.
When you subtract, everything from 0 to 4 cancels out because both sets contain them. What's left is only the subarrays with sum exactly 5

see [leet code binary sum](https://leetcode.com/problems/binary-subarrays-with-sum/)

The most natural way to solve this problem is with prefix sum though.
