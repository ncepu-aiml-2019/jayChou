n = int(input('请输入求解的范围：'))

numbers = [1 for i in range(n)]

for i in range(2, n):
    if numbers[i] != 0:
        j = 2
        while (j * i) < len(numbers):
            numbers[i*j] = 0
            j = j + 1

for i in range(2, n):
    if numbers[i] == 1:
        print(i)
