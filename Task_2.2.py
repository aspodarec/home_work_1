a = input('Введите значения списка через запятые :').split(',')
for b in range(0, len(a) - 1, 2):
    a[b], a[b + 1] = a[b + 1], a[b]
print(''.join(a))
