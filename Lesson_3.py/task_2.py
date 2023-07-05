# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

input_dict =    {"Petya": ("asd", "qwe", "zxczx", "qqq"),\
                        "Masha": ("zxczxc", "zxczx", "aaa"),\
                        "Vasya": ("zxczx", "qqq", "aaa")}

persons = []
for key, value in input_dict.items():
    persons.append(key)

dict_for_clothes_set = {persons[0]: set()}
map_cloth_to_count_persons = {}
for person in persons:
    dict_for_clothes_set[person] = set()
    for cloth in input_dict[person]:
        dict_for_clothes_set[person].add(cloth)

for person in persons:
    for cloth in dict_for_clothes_set[person]:
        if cloth not in map_cloth_to_count_persons:
            map_cloth_to_count_persons[cloth] = 1
        else:
            map_cloth_to_count_persons[cloth] = map_cloth_to_count_persons[cloth] + 1

# ✔ Какие вещи взяли все три друга
intersect = dict_for_clothes_set[persons[0]]
for person in persons:
    intersect = intersect.intersection(dict_for_clothes_set[person])
print(intersect)

# ✔ Какие вещи уникальны, есть только у одного друга
unique_set = set()
for cloth, count in map_cloth_to_count_persons.items():
    if count == 1:
        unique_set.add(cloth)
print(unique_set)

# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
count_persons = len(persons)
cloth_popular_list = []
cloth_popular_map = {}
for cloth, count in map_cloth_to_count_persons.items():
    if count == count_persons - 1:
        cloth_popular_list.append(cloth)

if cloth_popular_list:
    for cloth in cloth_popular_list:
        for person in persons:
            if cloth not in dict_for_clothes_set[person]:
                cloth_popular_map[cloth] = person
print(cloth_popular_map)