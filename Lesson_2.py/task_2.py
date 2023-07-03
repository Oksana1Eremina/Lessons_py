# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

import fractions

from math import gcd
 
n1, d1 = map(int, input("Введите первую дробь: ").split('/'))
n2, d2 = map(int, input("Введите вторую дробь: ").split('/'))
 
if d1 == d2:
    print('{}/{}'.format(n1+n2, d1))
else:
    cd = int(d1*d2/gcd(d1, d2))
    rn = int(cd/d1*n1+cd/d2*n2)
    g2 = gcd(rn, cd)
    n = int(rn/g2)
    d = int(cd/g2)
    print('{}/{}'.format(n, d) if n != d else n)

if d1 == d2:
    print('{}/{}'.format(n1*n2, d1*d2))
else:
    cd = int(d1*d2/gcd(d1, d2))
    rn = int(cd/d1*n1*cd/d2*n2)
    g2 = gcd(rn, cd)
    n = int(rn/g2)
    d = int(cd/g2)
    print('{}/{}'.format(n, d) if n != d else n)

firstfraction = fractions.Fraction(n1, d1)
secondfraction = fractions.Fraction(n2, d2)

res3 = firstfraction + secondfraction
res4 = firstfraction * secondfraction
print(res3)
print(res4)
