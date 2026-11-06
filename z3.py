s = input('Введите строку\n')
slova = s.split()
k = 0
for slovo in slova:
    if slovo[0] == 'е' or slovo[0] == 'Е':
        k += 1
print('Количество слов на букву "е":', k)