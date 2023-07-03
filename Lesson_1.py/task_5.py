import random
number=(random.randint(0, 1000))

a = 1000
b = 0
COUNT_TRY = 10
print(f"Угадай случайное число от {b} до {a}. Угадываем:")
while True:
    try:
        c = int(input())
        c = abs(c)
        if c != number:
            if c > number: 
                a=c
            else:
                b=c
            print(f"Неправильно, число находится в промежутке от {b} до {a}. Попробуй еще раз.")
                                                        
        else:          
            print("Ты угадал, поздравляю!")
            break
    except:
        print(f'Ошибка, вводи только целые числа.')        
        continue



   
