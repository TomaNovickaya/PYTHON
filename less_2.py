# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

print('Введите номер билета (6 цифр):')
a = int(input())
b = a%10
c = int(a/10%10)
d = int(a/100%10)
sum1= b + c + d
e = int(a/1000%10)
k = int(a/10000%10)
m=  int(a/100000%10)
sum2 = e + k + m
if sum1==sum2:
    print('YES')
else:
    print('NO')