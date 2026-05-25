with open('./study-notes/basic.md') as file:
    items = (i for i in file.readlines() if i.startswith('#'))

    for i in items:
        print(i)
