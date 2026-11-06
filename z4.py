n = int(input('Введите длину массива:'))
a = []
for i in range(n):
    print('Введите', i, 'элемент:')
    a.append(int(input()))
print('Исходный массив:', a)
maks = a[0]
for i in range(n):
    if a[i] > maks:
        maks = a[i]
print('Максимальный элемент:', maks)
print('Массив в обратном порядке:', a[::-1])