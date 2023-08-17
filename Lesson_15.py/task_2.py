# На семинаре про декораторы был создан логирующий декоратор.
# Он сохранял аргументы функции и результат её раблоты в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.

import json
from typing import Callable
from os.path import exists
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='logger.log')
log = logging.getLogger(__name__)


def logger(func: Callable):
    def wrapper(*args, **kwargs):
        info = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        info['result'] = result
        log.info(info)
        return result

    return wrapper


@logger
def get_sum(number1: int, number2: int, *args, **kwargs) -> int:
    return number1 + number2


if __name__ == '__main__':
    summ = get_sum(-5, -5, x=2, y='bye', z=False)
    print(summ)