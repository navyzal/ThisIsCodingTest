
N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(input()))

'''
15 14 
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
 
'''


count = 0

# 뚫린 곳 0, 막힌 곳 1, 방문한 곳 2
# 4방향/ 왼, 오, 위, 아래
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
    
def DFS(row, col):
    global graph, dr, dc
    
    graph[row][col] = '2'
    print(row, col, end=' - ')

    for idx in range(len(dr)):
        nr = row + dr[idx]
        nc = col + dc[idx]
        if 0 > nr or nr >= N or 0 > nc or nc >= M:
            continue
        if graph[nr][nc] == '0':
            DFS(nr, nc)

for r in range(N):
    for c in range(M):
        if graph[r][c] == '0':
            DFS(r,c)
            count += 1
            print()
     
print(count)
#print(graph)
