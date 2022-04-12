def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

def smart_divide(func):
    def inner(a, b):
        print(f"I am going to divide {a} and {b}")
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a, b)

    return inner

@smart_divide
def divide(a, b):
    return a/b

print(divide(2, 2))

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

# Chaining decorators
# The decorators are applied from top to bottom
@star
@percent
def printer(msg):
    print(msg)

printer("Hello")
