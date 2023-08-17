# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл
# Например, отлавливаем ошибку деления на ноль

import logging


def div_numbers(num_a: int, num_b: int) -> float:
    try:
        result = num_a / num_b
        return result
    except ZeroDivisionError as z:
        logging.basicConfig(level=logging.ERROR, filemode='a', filename='log1.log')
        logging.error('Нельзя делить на 0!')
        return float('inf')


if __name__ == '__main__':
    print(div_numbers(10, 3))
    print(div_numbers(10, 0))
