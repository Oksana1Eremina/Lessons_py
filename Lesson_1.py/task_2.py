a = int(input("Введите число от 1 до 100000: "))
while a <= 0 or a > 100000:
    print("AAA! Введите корректное число!")
    exit()
k = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        k = k+1
if (k <= 0):
    print("Число является простым")
else:
    print("Число является составным")