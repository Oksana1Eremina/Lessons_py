'''
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён
'''

from random import choices, randint
from string import ascii_lowercase, digits
import os

def gen_ext(ext: str, name_len_min: int=6, name_len_max: int=30, bytes_min: int=256, bytes_max: int=4096, num_files: int=42) -> None:
    for _ in range(num_files):
        name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(name_len_min, name_len_max)))
        data = bytes(randint(0, 255) for _ in range(randint(bytes_min, bytes_max)))
        name_with_ext = f'{name}.{ext}'
        if not os.path.exists(name_with_ext):
            with open(name_with_ext, 'wb') as f:
                f.write(data)
        

def gen_files_to_dir(dir: str):
    print("Current working directory: {0}".format(os.getcwd()))
    try:
        os.chdir(dir)
        print("Current working directory: {0}".format(os.getcwd()))
        gen_ext('txt')
    except FileNotFoundError:
        print("Directory: {0} does not exist".format(dir))
    except NotADirectoryError:
        print("{0} is not a directory".format(dir))
    except PermissionError:
        print("You do not have permissions to change to {0}".format(dir))

if __name__ == '__main__':
    gen_files_to_dir('dir1')