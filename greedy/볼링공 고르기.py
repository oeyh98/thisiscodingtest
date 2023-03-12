from collections import deque

n, m = map(int, input().split())
lst = list(map(int, input().split()))
result = 0
weight = [0] * (m+1)

for i in lst:
    weight[i] += 1

for i in range(1, m+1):
    n -= weight[i]
    result += (weight[i] * n)


