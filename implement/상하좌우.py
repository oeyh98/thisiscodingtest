n = int(input())
move = list(input().split())
current = [1, 1]

for m in move:
    if m == "L" and current[1] > 1:
        current[1] -= 1
    elif m == "R" and current[1] < n+1:
        current[1] += 1
    elif m == "U" and current[0] > 1:
        current[0] -= 1
    elif m == "D" and current[0] < n+1:
        current[0] += 1

print(*current, end=" ")