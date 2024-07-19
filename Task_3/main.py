# Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
# Скрипт повинен приймати не обов'язковий аргумент командного рядка, після аргументу шляху до файлу логів. Він відповідає за виведення всіх записи певного рівня логування. І приймає значення відповідно до рівня логування файлу. Наприклад аргумент error виведе всі записи рівня ERROR з файлу логів.
# Скрипт має зчитувати і аналізувати лог-файл, підраховуючи кількість записів для кожного рівня логування (INFO, ERROR, DEBUG, WARNING).
# Реалізуйте функцію parse_log_line(line: str) -> dict для парсингу рядків логу.
# Реалізуйте функцію load_logs(file_path: str) -> list для завантаження логів з файлу.
# Реалізуйте функцію filter_logs_by_level(logs: list, level: str) -> list для фільтрації логів за рівнем.
# Реалізуйте функцію count_logs_by_level(logs: list) -> dict для підрахунку записів за рівнем логування.
# Результати мають бути представлені у вигляді таблиці з кількістю записів для кожного рівня. Для цього реалізуйте функцію display_log_counts(counts: dict), яка форматує та виводить результати. Вона приймає результати виконання функції count_logs_by_level.
from pathlib import Path



def parse_log_line(line: str) -> dict:
    pass
    #приймає рядок з логу як вхідний параметр і повертає словник з розібраними компонентами: дата, час, рівень, повідомлення. 
    #Використовуйте методи рядків, такі як split(), для розділення рядка на частини.
    res = [lines.split() for lines in line ]

def load_logs(file_path: str) -> list:
    pass
    # відкриває файл, читає кожен рядок і застосовує на нього функцію parse_log_line, зберігаючи результати в список.
def filter_logs_by_level(logs: list, level: str) -> list:
    pass


def count_logs_by_level(logs: list) -> dict:
    pass


def display_log_counts(counts: dict):
    # форматує та виводить результати. Ф-я приймає результати виконання функції count_logs_by_level.
    pass