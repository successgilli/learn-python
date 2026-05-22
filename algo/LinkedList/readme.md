## LinkedLists
A `linkedList` is a similar data structure to an array only that instead of items sitting contiguous to each other in memory, they are objects pointing to each other via a pointer property say `next`.

                    (1) -> (2) -> (3)

Sample linkedList structure
```py
class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

node1 = Node(1)
node2 = Node(2)

node1.next = node2
head = node1

print(head.val)
print(head.next.val)
```

### Traversal
We can traverse a linkedlist like so

```py
class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = val

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

head = node1
```

### Singly and doubly linkedList
The difference is that with doubly linkedLists, you have `prev`.

So at a node, you have both prev and next. with sinlgy linked lists, you may need a reference at `i-1` for certain operations. With doubly linked lists, you only need the node at `i`.

### Fast and Slow Pointers.
Fast and slow pointers is a concept that builds on the two pointer algorithm and allows us to solve a variation of linkedList problems elegantly.

It centers around the idea that one pointer simply moves faster than the other and coordinate to solve a given problem.

Sample problems include:
### Find middle of the list
With fast and slow pointers, we can solve this without having to first cheat by counting the entire items in the list and then moving to a specific count.

We simple set a fast pointer moving twice the speed of a slow pointer. Mathematically, by the time the fast pointer is at the end of the list. The slow pointer should be at the middle of the list.

### Find kth node from the end
Simply start by moving a fast point `k` positions forward.
Now, fast is `k` ahead of slow. now, move both at same speed until fast reaches the end. at this point, slow is `k` positions from the end of the LinkedList.

### Detect cycle in linkedList
The idea is that if one pointer moves faster than the other, then if there is a cycle, they will eventually meet.

simply move one pointer, say, twice as fast as the slow pointer. If they meet during the traversal at some point, there is a cycle but if we reach the end of the list, there is no cycle.

### Detect start of cycle in linkedList
This is a modification of the above counterpart.

**Math behidn the problem**:

For this problem:
x1 = distance from head to start of circle
x2 = perimeter of circle
x3 = meeting point from start of circle.

slow at meeting point traveled => `X1 + X3`
as such, if fast is moving 2 times faster we can say fast traveled =>  `2(X1 + X3)`

Also, we can say fast total distance covered is =>` X1 + nX2 + X3`. here `n` is number of times it went round based on the length of the circle and speed.

therefore: `2(X1 + X3) = X1 + nX2 + X3`

This then breaks down to: `X1 = nX2 - X3` meaning they are at a meeting point `x3` from the start of the loop (already known above).

To make it clearer, `X2` is perimeter of the circle. We will introduce a new variable to complete the definition of a perimeter.
perimeter `X2 = X3 + remainingDistanceToStart`.
Equation becomes: `X1 = n(X3 + remainingDistanceToStart) - X3`. we are in a loop, so we can consider n=1 to make our solution obvious for constant distance.
`X1 = X3 + remainingDistanceToStart - X3 = remainingDistanceToStart`
Finally: `X1 = remainingDistanceToStart`. The distance from head to start of circle is equal to the remaining distance from meeting point to start of cycle/circle. 

For two items running from a point into a circle where one moves faster than the other, we can conclude that at a meeting point in the circle, distance from head to start of cycle is equal to the distance from meeting point to start of cycle.

So at this point, since distance is equal, at same speed, they should meet at the start.

**Solution**:
- Move one faster than the other till cycle is detected
- At meeting point, take one pointer back to the head.
- now move both pointers one node at a time till they meet.
- the point of meeting is the start of the cycle.

These and many more similar problems simply leverage the fast and slow pointers concept.

## Tips
- For reversal, we need the `prev` not `next`. Hold a pointer to `prev` in combination to `current head`.
