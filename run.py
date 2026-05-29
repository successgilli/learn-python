class MyManager():
    '''
    My manager haha
    '''
    def __init__(self, startCount: int):
        self.startCount = startCount
        self.items = [startCount]
    
    def __enter__(self):
        print('entering')
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        print('exiting')
        print(self.items)
        return True # Decides if errors are propagated should they happen during resource usage
    
    def do(self, item):
        print(f'doing {item}')
        self.items.append(item)

items = [284,4,2,5,3]

with MyManager(3) as resource:
    for item in items:
        resource.do(item)
    
    raise Exception('bla')

