'''Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
✔ При достижении конца более короткого файла, возвращайтесь в его начало.
'''

def convert(names_file: str, nums_file: str, result_file: str):
    with open(names_file, 'r', encoding='UTF-8') as f_names, open(nums_file, 'r', encoding='UTF-8') as f_nums, open(result_file, 'w', encoding='UTF-8') as f_res:
        data_nums = f_nums.readlines()
        data_names = f_names.readlines()
        data_nums_len = len(data_nums)
        data_names_len = len(data_names)
        max_len = max(data_nums_len, data_names_len) 
        for i in range (max_len): 
            data_nums_index = i % data_nums_len
            data_names_index = i % data_names_len
            int_value, float_value = data_nums[data_nums_index].split('|')
            int_value = int(int_value)
            float_value = float(float_value)
            mult_res = int_value * float_value
            if mult_res < 0:
                result = data_names[data_names_index].lower() + ' ' + str(abs(mult_res))
            else:
                result = data_names[data_names_index].upper() + ' ' + str(round(mult_res))
            f_res.write(result + '\n')
        
if __name__ == '__main__':
    convert('task2_result.txt', 'task_1.txt', 'task_3.txt')