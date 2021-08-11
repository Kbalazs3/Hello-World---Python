
def get_hello_message():
    name = input("Enter your name: ")
    return name


def say_hello(name):
    if not name:
        print("Hello world!")
    else:
        print(f'Hello {name}!')


say_hello(get_hello_message())
