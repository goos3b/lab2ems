n = int(input('Введите длину массива:'))
a = []
for i in range(n):
    print('Введите', i, 'элемент:')
    a.append(float(input()))
print('Исходный массив:', a)
summa = 0
for i in range(n):
    summa = summa + a[i]
srednee = summa / n
for i in range(n):
    if a[i] == 0:
        a[i] = srednee
print('Полученный массив:', a)