import random


def log(output_pattern: str):
    def log_wrapper(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(output_pattern.format(random.randint(300, 600)))
            return result
        return wrapper
    return log_wrapper
