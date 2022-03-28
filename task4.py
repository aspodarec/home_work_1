number = input("введите положительное целое число")
length = len(number)
max = 0
count = 0

while count < length:
    val = int(number[count])
    if val > max:
        max = val
    count += 1

print(max)