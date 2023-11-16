import random


def log(output_pattern: str):
    """
    Декоратор для логирования.

    Args:
    output_pattern (str): Шаблон строки для вывода, который должен содержать
                          один форматируемый параметр для случайного числа.

    Returns:
    function: Функция-обёртка, которая добавляет логирование к вызываемой
    функции.
    """
    def log_wrapper(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(output_pattern.format(random.randint(300, 600)))
            return result
        return wrapper
    return log_wrapper


def dict_to_str(dictionary: dict):
    """
    Конвертирует словарь в строку формата ключ-значение.

    Args:
    dictionary (dict): Словарь для конвертации.

    Returns:
    str: Строка, представляющая содержимое словаря в формате 'ключ: значение'.
    """
    return '\n'.join(f'{key}: {value}' for key, value in dictionary.items())
