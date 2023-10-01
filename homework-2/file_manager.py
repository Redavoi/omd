from storage_csv import StorageCSV
from typing import Dict


class FileManager:
    """
    Класс для работы с файлами.
       Methods:
           read_csv(file_path: str) -> StorageCSV:
               Читает сsv файл  и возвращает StorageCSV.

           write_csv(file_path: str, data: str):
               Записывает данные data в файл file_path
    """
    @staticmethod
    def read_csv(file_path: str) -> StorageCSV:
        """
        Читает csv файл и возвращает данные в виде StorageCSV класса.
        Args:
            file_path: str, путь к файлу который нужно прочитать.

        Returns:
            StorageCSV: представление csv данных в формате класса StorageCSV.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            file_lines = file.readlines()
            columns_name = list(map(str.strip, file_lines[0].split(';')))
            file_dict_representation: Dict[int, Dict[str, str]] = {}

            for line_idx, file_line in enumerate(file_lines):
                if line_idx > 0:
                    file_dict_representation[line_idx] = {}
                    line_elements = file_line.split(';')
                    for line_element_idx, line_element in enumerate(line_elements):
                        file_dict_representation[line_idx][columns_name[line_element_idx]] = line_element.strip()

            return StorageCSV(columns_name, file_dict_representation)

    @staticmethod
    def write_csv(file_path: str, data: str) -> None:
        """
        Записывает данные в файл.
        Args:
            file_path: str, путь к файлу для записи.
            data: str, данные для записи.

        Returns:
            None
        """
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
