import time
def decorator_fucntion(func):
    def wrapper_function():
        time.sleep(2)
        func()
    return wrapper_function

@decorator_fucntion
def say_hello():
    print("Hello")

@decorator_fucntion
def say_bye():
    print("Bye")


say_bye()