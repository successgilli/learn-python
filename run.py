try:
    raise Exception('haha')
except Exception as e:
    print(e.args[0])