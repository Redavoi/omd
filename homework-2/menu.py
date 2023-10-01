from menu_mode import MenuMode
from department_hierarchy import write_department_hierarchy
from department_report import write_department_report, save_department_report
from file_manager import FileManager
from storage_csv import StorageCSV


def execute_menu_mode(*, menu_mode: MenuMode, data: StorageCSV) -> None:
    """
    Вызывает функции из меню, в зависимости от выбранного номер.
    Args:
        menu_mode: MenuMode, номер функции которую нужно выполнить.
        data: StorageCSV, представление csv данных в формате класса StorageCSV.

    Returns:
        None
    """
    match menu_mode:
        case MenuMode.WRITE_DEPARTMENT_HIERARCHY:
            write_department_hierarchy(data)
        case MenuMode.WRITE_REPORT:
            write_department_report(data)
        case MenuMode.SAVE_REPORT:
            save_department_report(data)
        case MenuMode.EXIT:
            exit()
        case _:
            print('Режим с таким номером отсутствует, попробуйте еще раз')


def print_menu_instructions() -> None:
    """
    Выводит меню.
    Returns:
        None
    """
    print('Выберите:\n'
          '1. Получения иерархии команд у департаментов.\n'
          '2. Получение сводного отчета по департаментам.\n'
          '3. Сохранение сводного отчета по департаментам.\n'
          '4. Выход.\n')


def menu_interact(file_path: str) -> None:
    """
    Ввод номера функции и передача этого значения дальше в execute_menu_mode.
    Args:
        file_path: str, путь к файлу где хранятся данные для обработки.

    Returns:
        None
    """
    print_menu_instructions()

    data = FileManager.read_csv(file_path)
    while (input_value := int(input('Your menu choice: '))) != MenuMode.EXIT:
        if MenuMode.is_in(input_value):
            menu_mode = MenuMode(input_value)
            execute_menu_mode(menu_mode=menu_mode, data=data)
        else:
            print('Режим с таким номером отсутствует, попробуйте еще раз')

        print_menu_instructions()
