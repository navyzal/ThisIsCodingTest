
location = list(input())

x = ord(location[0]) - ord('a') + 1
y = int(location[1])

dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [ -1, 1, -1, 1, -2, 2, -2, 2]

count = 0

#for i in range(N)
for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or nx > 9:
        continue
    if ny < 1 or ny > 9:
        continue
    count += 1

print(count)