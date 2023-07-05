# Дан список повторяющихся элементов. 
lst = ['1', '1', '2', '2', '3', '4', '4', '5']

# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.
map = {}
for item in lst:
    if item not in map:
        map[item] = 1
    else:
        map[item] = map[item] + 1

result = []
for item in lst:
    if map[item] > 1:
        result.append(item)
        map[item] = 0
print(result)