a = enumerate(input('Введите данные:').split())
for i, c in a:
    print(i+1, c[:10])