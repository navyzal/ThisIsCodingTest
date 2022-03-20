from ctypes.wintypes import CHAR


size = int(input())
direction = input().split()
size = len(direction)

currentR = 1
currentC = 1

'''무식하게...
for c in direction:
    if c == 'L':        
        currentC -= 1
        if currentC < 1:
            currentC = 1
    elif c == 'R':
        currentC += 1
        if currentC > size:
            currentC = size
    elif c == 'U':
        currentR -= 1
        if currentR < 1:
            currentR = 1

    elif c == 'D':
        currentR += 1
        if currentR > size:
            currentR = size
        
'''

# 우아하게...

# L R U D
dr = (0, 0, -1, 1)
dc = (-1, 1, 0, 0)
move_type = ('L','R','U','D')

for d in direction:
    for i in range(len(move_type)):
        if d == move_type[i]:
            nc = currentC + dc[i]
            nr = currentR + dr[i]
            if nc < 1 or nc > size or nr > size or nr < 1:
                continue
            currentC = nc
            currentR = nr



print(currentR, currentC)

#print(direction)