import time
from functools import wraps


def log(filename=None):
    """Декоратор, который будет автоматически регистрировать детали выполнения функций,
    такие как время вызова, имя функции, передаваемые аргументы, результат выполнения и информация об ошибках."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                success_message = (
                    f"Start: {start_time}. {func.__name__} completed successfully. Result: {result}. End: {end_time}"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(success_message + "\n")
                else:
                    print(success_message)
                return result
            except Exception as e:
                error_message = f"Error in {func.__name__}: {type(e).__name__}. Input: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as text:
                        text.write(error_message + "\n")
                else:
                    print(error_message)

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(4, 2)
my_function(
    4,
)
