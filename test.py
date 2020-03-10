def hello_world(args):
    try:
        print(eval('args'))
        return True
    except Exception as e:
        passs
hello_world('test')
