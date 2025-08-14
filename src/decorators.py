from functools import wraps


def log(filename=None):
    """Декоратор, который будет автоматически регистрировать детали выполнения функций,
    такие как время вызова, имя функции, передаваемые аргументы, результат выполнения и информация об ошибках."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                success_message = f"{func.__name__} ок. Результат : {result}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(success_message + "\n")
                else:
                    print(success_message)
                return result
            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Input: {args}, {kwargs}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as text:
                        text.write(error_message + "\n")
                else:
                    print(error_message)

        return wrapper

    return decorator
