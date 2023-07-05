# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
set = {'clock': 2, 'apple': 1, 'bike': 10, 'table': 10, 'can': 3}

def pack_backpack(capacity: int, set: dict):
    packaging_option = []
    for key, value in set.items():
        if value <= capacity:
            capacity -= value
            packaging_option.append(key)
    return packaging_option


print(pack_backpack(15, set))