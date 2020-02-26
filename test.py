


def hello_world(args):
    try:
        print(eval('args'))
        return True
    except:
        pass
    while True:
        response = input('Enter the hash that follows ' + lastkey + ': ')
        result = hashlib.new(ALGORITHM, response.encode()).hexdigest()


hello_world("test")
