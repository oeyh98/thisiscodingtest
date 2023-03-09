n = int(input())

coin = [500, 100, 50, 10]
cnt = 0

for c in coin:
    cnt = cnt + (n//c)
    n = n%c

print(cnt)
