'''
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки
'''

import os

VIDEO_EXTS = ['mp4', 'avi']
TEXT_EXTS = ['txt', 'doc']
MUSIC_EXTS = ['mp3']
PICTURE_EXTS = ['jpg', 'png']

def sort_files_to_dirs_by_exts():
    os.mkdir('video')
    os.mkdir('text')
    os.mkdir('music')
    os.mkdir('picture')
    
    for name in os.listdir():
        if os.path.isfile(name):
            _, ext = name.split(".")
            if ext in VIDEO_EXTS:
                os.replace(name, "video/" + name)
            if ext in TEXT_EXTS:
                os.replace(name, "text/" + name)
            if ext in MUSIC_EXTS:
                os.replace(name, "music/" + name)
            if ext in PICTURE_EXTS:
                os.replace(name, "picture/" + name)

if __name__ == '__main__':
    sort_files_to_dirs_by_exts()