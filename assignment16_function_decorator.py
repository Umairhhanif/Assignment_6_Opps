def log_function_call(func):

    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

# Applying the decorator to a function
@log_function_call
def say_hello(name):
    print(f"Hello, {name}!")
# Calling the decorated function
say_hello("Mohammad Umair") 