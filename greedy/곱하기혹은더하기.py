n = list(map(int, input()))
result = 0
for i in n:
    if result <= 1 or i <= 1:
        result += i
    else:
        result *= i


print(result)
