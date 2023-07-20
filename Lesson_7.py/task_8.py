'''
✔ Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

'''

import os

def group_rename(name_addition: str='', width: int=3, ext: str='txt', new_ext: str='txt', l_bound: int=3, r_bound: int=6):
    counter = 1
    for name in os.listdir():
        if os.path.isfile(name):
            file_name, file_ext = name.split(".")
            if file_ext == ext:
                new_file_name = file_name[l_bound-1:r_bound-len(file_name)] + name_addition + '{num:0{width}}'.format(num=counter, width=width) + '.' + new_ext
                counter+=1
                os.replace(name, new_file_name)


if __name__ == '__main__':
    group_rename(name_addition='add_',new_ext='ini')