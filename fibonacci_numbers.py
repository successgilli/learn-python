# The fib numbers is a sequence of numbers where each number is a sum of the preceeding two numbers.
# This sequence starts with 0 and 1
# E.G: 0, 1, 1, 2, 3, 5, 8, 13,...

def fib(n = 50):
    x,y = 0,1
    items = []

    while x < n:
        items.append(x)
        x,y = y, x+y
    
    print(items)

fib()
