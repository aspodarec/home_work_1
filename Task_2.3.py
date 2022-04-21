seasons = {
    'Зима': ['12', '1', '2'],
    'Лето': ['6', '7', '8'],
    'Осень': ['9', '10', '11'],
    'Весна': ['3', '4', '5']
}
month = input("Введите порядковый номер месяца: ")
for month_user in seasons:
    if seasons[month_user].count(month):
        print(month_user);
