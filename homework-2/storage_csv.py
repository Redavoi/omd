from typing import List, Dict
from dataclasses import dataclass


@dataclass
class StorageCSV:
    """
    Класс для представления данных из csv файлп.

    Attributes:
        columns_name (List[str]): список, который хранит названия столбцов.
        file_dict_representation (Dict[int, Dict[str, str]]): представляет
            словарь данных - ключем является номер строки в csv файле,
            значение - словарь у которого ключ это название столбца,
            а значение - что хранится в этом столбце.
    """
    columns_name: List[str]
    file_dict_representation: Dict[int, Dict[str, str]]
