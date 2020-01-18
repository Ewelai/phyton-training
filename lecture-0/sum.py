n = int(input('Enter the number: '))
sum = 0.0

for i in range(1, n):
    sum += 1 / (2 ** i)
print(sum)
