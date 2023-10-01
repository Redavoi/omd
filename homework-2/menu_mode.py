from enum import Enum


class MenuMode(Enum):
    """
    Класс хранящий номера режимов для выбора в меню.
    Methods:
        is_in(cls, value: int) -> bool
            Проверяет - находится ли атрибут с значением value внутри класса.
    """
    WRITE_DEPARTMENT_HIERARCHY = 1
    WRITE_REPORT = 2
    SAVE_REPORT = 3
    EXIT = 4

    @classmethod
    def is_in(cls, value: int) -> bool:
        """
        Проверяет - находится ли атрибут с значением value внутри класса.
        Args:
            value: int, значение, которое нужно проверить

        Returns:
            bool: результат поиска, True - значение было найдено, иначе False.
        """
        return value in [member.value for member in cls]
