# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.

# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.

# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.

# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.


"""
При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значение `n`

При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `n` для проверки
"""

n = 123456

# Введите ваше решение ниже

if n//100000 +(n//10000)%10 + (n//1000)%10 == (n%1000)//100 +(n%100)//10 + n%10:
    print('yes')
else:
    print('no')