from enum import Enum


class ColumnNameIdx(Enum):
    """
    Класс, который задает индексы столбцов - на каком месте идет название
    данного столбца в csv файле.
    """
    FULLNAME = 0
    DEPARTMENT = 1
    COMMAND = 2
    JOB_POSITION = 3
    ASSESSMENT = 4
    SALARY = 5
