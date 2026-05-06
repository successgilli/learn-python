print(abs(-3))
x = y = 3

if not None:
    x //= 2
    print(f'{x} yaa')

if x > 1:
    print("bla")
    pass # do something
elif x < 1:
    print("bla2")
    pass # do something else
else:
    print("bla3")
    pass # conclude

val = 3 if x == 1 else 4

print(val)

while (y := x * 3) > 1:
    print(y, " here")
    break
    x -= 1
else:
    print("done")

for x in range(10):
    print(x)
    break
else:
    print("done 2")
