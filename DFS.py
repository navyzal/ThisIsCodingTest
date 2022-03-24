
# https://www.notion.so/DFS-dd0e006817104511a4fdf1cb2f199d0e

from collections import deque

graph = [[],  # 0부터 시작...
       [2, 3, 8],
       [1,7],
       [1,4,5],
       [3,5],
       [3,4],
       [7],
       [2,6,8],
       [1,7]]

visited = [False for _ in range(len(graph))]

def dfs(idx):
    global graph
    global visited
    visited[idx] = True
    print(idx, end=' ')       
    for i in graph[idx]:
        if not visited[i]:                     
            dfs(i)

dfs(1)
print()