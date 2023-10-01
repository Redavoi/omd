from dataclasses import dataclass
from typing import Dict

from column_name_idx import ColumnNameIdx
from file_manager import FileManager
from storage_csv import StorageCSV
from utils import recalculate_avg


@dataclass
class DepartmentReport:
    """
    Класс содержит информацию, которая должна быть в сводном
    отчете по департаментам.

    department - название департамента.
    stuff_number - количество работников в департаменте.
    min_salary - минимальная зарплата в департаменте.
    max_salary - максимальная зарплата в департаменте.
    avg_salary - средняя зарплата в департаменте.
    """
    department: str
    stuff_number: int
    min_salary: float
    max_salary: float
    avg_salary: float


def get_department_report(data: StorageCSV) -> Dict[str, DepartmentReport]:
    """
    Получает сводный отчет по каждому департаменту.
    Args:
        data: StorageCSV, представление csv данных в формате
            класса StorageCSV.

    Returns:
        Dict[str, DepartmentReport]: содержит в качестве ключа - название
            департамента, в качестве значения - сводный отчет.
    """
    department_report: Dict[str, DepartmentReport] = {}
    person_information_pool = list(data.file_dict_representation.values())

    for persons_information in person_information_pool:
        department_column_name = data.columns_name[ColumnNameIdx.DEPARTMENT.value]
        department_name = persons_information[department_column_name]

        salary_column_name = data.columns_name[ColumnNameIdx.SALARY.value]
        person_salary = float(persons_information[salary_column_name])

        department_report.setdefault(department_name, DepartmentReport(department=department_name,
                                                                       stuff_number=0,
                                                                       min_salary=float('inf'),
                                                                       max_salary=0,
                                                                       avg_salary=0))

        department_report[department_name].stuff_number += 1
        if department_report[department_name].min_salary > person_salary:
            department_report[department_name].min_salary = person_salary

        if department_report[department_name].max_salary < person_salary:
            department_report[department_name].max_salary = person_salary

        department_report[department_name].avg_salary = recalculate_avg(
            old_avg=department_report[department_name].avg_salary,
            new_value=person_salary,
            old_avg_elements_count=department_report[department_name].stuff_number)

    return department_report


def write_department_report(data: StorageCSV) -> None:
    """
    Получает сводные отчеты по департаментам и печатает их.
    Args:
        data: StorageCSV, представление csv данных в формате
        класса StorageCSV.

    Returns:
        None
    """
    department_report = get_department_report(data)
    for department in department_report:
        print(f'Department name: {department}\n'
              f'Stuff number: {department_report[department].stuff_number}\n'
              f'Min salary: {department_report[department].min_salary}\n'
              f'Max salary: {department_report[department].max_salary}\n'
              f'Average salary: {department_report[department].avg_salary}\n')


def save_department_report(data: StorageCSV) -> None:
    """
    Получает сводные отчеты по всем департаментам и сохраняет их в csv
    формате в файл department_report.csv .
    Args:
        data: StorageCSV, представление csv данных в формате
        класса StorageCSV.

    Returns:
        None
    """
    department_report_csv = 'Department_name;Stuff_number;Min_salary;Max_salary;Average_salary\n'
    department_report = get_department_report(data)
    for department in department_report:
        department_report_csv += f'{department};' \
                                 f'{department_report[department].stuff_number};' \
                                 f'{department_report[department].min_salary};' \
                                 f'{department_report[department].max_salary};' \
                                 f'{department_report[department].avg_salary}\n'

    FileManager.write_csv('department_report.csv', department_report_csv)
