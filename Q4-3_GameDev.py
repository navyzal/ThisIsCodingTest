'''
4 4  
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''

#N x M ()
N, M = map(int, input().split())
X, Y, D = map(int, input().split())

m = []

for i in range(M):
    m.append(list(map(int, input().split())))

# N W S E
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def turnLeft():
    global D
    D = (D + 1) % 4
    print(D)

tCount = 0
count = 0

while True:
    if tCount == 4:
        X -= dx[D]
        Y -= dy[D]
        if m[Y][X] == 1:
            break
        else:
            tCount = 0

    turnLeft()

    if m[Y + dy[D]][X + dx[D]] == 0:
        X += dx[D]
        Y += dy[D]
        m[Y][X] = 2
        tCount = 0
        count += 1
        
    else:
        tCount += 1        

print(count)