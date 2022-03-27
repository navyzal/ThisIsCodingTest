from collections import deque

'''
5 6
101010
111111
000001
111111
111111
'''

N, M = map(int, input().split())

maze = []
for i in range(N):
    maze.append(list(map(int, input())))
    

# 왼 오 위 아래
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]    

queue = deque()
'''
def BFS(row, col):
    global maze, dr, dc, count
    if row == N-1 and col == M-1:
        queue.clear
        count += 1
        return
    
    for i in range(len(dr)):
        nr = row + dr[i]
        nc = col + dc[i]
        isFound = False
        
        if nr < 0 or nr >= N:
            continue
        
        if nc < 0 or nc >= M:
            continue
        
        if maze[nr][nc] != 0:            
            isFound = True
            maze[nr][nc] = 0
            queue.append((nr, nc))
            BFS(nr, nc)
        
        if isFound:
            count += 1
            isFound = False
    
    if queue:    
        nc, nr = queue.popleft()
        print(nc, nr)
        BFS(nr, nc)

maze[0][0]=0
'''
#queue.append((0,0))

# 괴물 0
def BFS(row, col):
    global dc, dr
    queue = deque()
    queue.append((row, col))
    count = 1
        
    while queue:
        row, col = queue.popleft()
        count = maze[row][col]
        
        if (row, col) == (N-1, M-1):
            return count
        
        for i in range(len(dr)):
            nr = row + dr[i]
            nc = col + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if maze[nr][nc] == 0:
                continue
            if maze[nr][nc] == 1:
                maze[nr][nc] = count+1
                queue.append((nr,nc))
        

print(BFS(0,0))