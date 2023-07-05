# Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# ✔ Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

str = input("Введите строку: ")
print(str)

map1 = {}
map2 = {}

for symbol in str:
    if symbol not in map1:
        map1[symbol] = 1
        map2[symbol] = str.count(symbol)
    else:
        map1[symbol] = map1[symbol] + 1

print(map1)
print(map2)

# Порядок ключей совпадает, потому что при выводе словаря они сортируются.