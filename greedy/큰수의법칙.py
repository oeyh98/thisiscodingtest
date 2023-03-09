import sys

n, m, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num.sort()
data = [num[-1], num[-2]]

s = [0, 0, 0, 1]
cnt = 0
result = 0

for _ in range(m):
    result += data[s[cnt]]
    cnt = cnt+1 if cnt<3 else 0

print(result)