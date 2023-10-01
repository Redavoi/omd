from storage_csv import StorageCSV
from column_name_idx import ColumnNameIdx
from typing import Dict, List


def get_department_hierarchy(data: StorageCSV) -> Dict[str, List[str]]:
    """
    Функция которая получает иерархичное представление команд в
    депертаменте. Для каждого департамента собираются все группы,
    которые в нем есть.
    Args:
        data: StorageCSV, представление csv данных в формате
        класса StorageCSV.

    Returns:
        Dict[str, List[str]]: словарь, где ключ - название департамента,
            значение - список уникальных команд департамента.
    """
    department_and_command: Dict[str, List[str]] = {}
    person_information_pool = list(data.file_dict_representation.values())

    for persons_information in person_information_pool:
        department_column_name = data.columns_name[ColumnNameIdx.DEPARTMENT.value]
        department_name = persons_information[department_column_name]
        department_and_command.setdefault(department_name, [])

        command_column_name = data.columns_name[ColumnNameIdx.COMMAND.value]
        command_name = persons_information[command_column_name]
        if command_name not in department_and_command[department_name]:
            department_and_command[department_name].append(command_name)

    return department_and_command


def write_department_hierarchy(data: StorageCSV) -> None:
    """
    Выполняет get_department_hierarchy и делает print полученных данных.
    Args:
        data: StorageCSV, представление csv данных в формате класса StorageCSV.

    Returns:
        None
    """
    department_and_command = get_department_hierarchy(data)

    for department_name in department_and_command:
        command_names = department_and_command[department_name]
        command_names_str = '\t\t\t\t\t\t'.join([command_name + '\n'
                                                 for command_name in command_names])

        print(f'Department name: {department_name}\n\t\t\t\t\t\t{command_names_str}')
