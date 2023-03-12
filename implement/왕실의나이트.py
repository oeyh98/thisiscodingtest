n = input()
x = ["a", "b", "c", "d", "e", "f", "g", "h"]
y = [1, 2, 3, 4, 5, 6, 7, 8]

current = [x.index(n[0]), int(n[1])-1]
move = [[-2, -1], [-2, 1], [-1, -2], [1, -2], [2, -1], [2, 1], [-1, 2], [1, 2]]
cnt = 0

for m in move:
    nx = current[0] + m[0]
    ny = current[1] + m[1]

    if 0 <= nx <= 7 and 0 <= ny <= 7:
        cnt += 1

print(cnt)
