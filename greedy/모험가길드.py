import sys

n = int(sys.stdin.readline())
fear = list(map(int, sys.stdin.readline().split()))
cnt = 0
result = 0
fear.sort()
guild = [] * n

for f in fear:
    cnt += 1
    if cnt >= f:
        result += 1
        cnt = 0

print(result)

#참고 https://wooono.tistory.com/539