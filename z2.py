vsego = 0        # сколько чисел ввели
nakopitel = 0    # их сумма

print('Вводи числа по одному. Ноль — конец ввода.')
chislo = int(input('Число: '))

while chislo != 0:
    nakopitel += chislo
    vsego += 1
    chislo = int(input('Число: '))

print('Сумма всех чисел:', nakopitel)
print('Всего чисел:', vsego)