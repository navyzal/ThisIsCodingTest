from ctypes.wintypes import CHAR


size = int(input())
direction = input().split()
size = len(direction)

'''무식하게...
currentR = 1
currentC = 1

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
        
print(currentR, currentC)
'''

# 우아하게...

# L R U D
dc = (0, 0, -1, 1)
dr = (-1, 1, 0, 0)
move_type = ('L','R','U','D')

for 




#print(direction)