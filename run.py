import sys

class A:
    __slots__ = ('name', 'title')
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def cry(self):
        print('😭')
    
    def shout(self):
        print('🤯')
    
    def greet(self):
        print('Hello')

class B:
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def cry(self):
        print('😭')
    
    def shout(self):
        print('🤯')
    
    def greet(self):
        print('Hello')
    
a = A('Ben', 'Benito')
b = B('Ben', 'Benito')
print(A.__dict__)
print(B.__dict__)
print(f'Size of instance a is {sys.getsizeof(A)} bytes')
print(f'Size of instance b is {sys.getsizeof(B)} bytes')
