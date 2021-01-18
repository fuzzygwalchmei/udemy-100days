import time

current_time = time.time()

print(current_time)

def speed_calc_decorator(func):
    def wrapper():
        start = time.time()
        func()
        time_taken = time.time() - start
        print(f"{func.__name__} run speed: {time_taken}")
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(10_000_000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100_000_000):
        i * i

fast_function()
slow_function()