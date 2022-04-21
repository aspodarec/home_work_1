import math

time = int(input('введите время в секундах'))
hours = time // 3600
hours_ost = (time % 3600)
min = hours_ost // 60
sec = hours_ost % 60
print(f"{hours}:{min}:{sec}")
