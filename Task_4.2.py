a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
answer = []

for i in range(len(a)-1):
    if a[i] < a[i+1]:
        answer.append(a[i+1])

print(answer)
