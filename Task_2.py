from typing import Callable
from decimal import Decimal
import re


def generator_numbers(text: str):
    # Фукнція перевіряє в тексті наявність цілих чисел, перетворює кожен рядок в Decimal та повертає генератор
    pattern = r'\d+\.\d+'
    matches = re.findall(pattern, text)
    for match in matches:
        yield Decimal(match)
    

def sum_profit(text: str, func: Callable)-> Decimal:
    # Підрахунок суми знайдених генератором цілих чисел з тексту
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
