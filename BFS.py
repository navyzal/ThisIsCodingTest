
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

# 1. 근처 방문 노드를 큐에다가 집어 넣는다.
# 2. 큐에서 depeue 를 하고, dequeue 한 곳의 주변 중 아직 방문 하지 않은 곳을 큐에 집어 넣는다.
# 3. 큐가 다 비어지면 끝



''' 재귀 구현 
 재귀 함수로 DFS를 구현하면 컴퓨터 시스템의 동작 특성상 실제 프로그램의 수행 시간은 느려질 수 있다.
 따라서 스택 라이브러리를 이용해 시간 복잡도를 완화하는 테크닉이 필요할 때도 있다.
queue = deque()
def bfs(idx):
    global graph
    global visited
    if not visited[idx]:
        print(idx, end= ' ')
        visited[idx] = True
        queue.append(idx)
    
    for i in graph[idx]:
        if not visited[i]:
            visited[i] = True
            queue.append(i)
            print(i, end=' ')
    if queue:
        bfs(queue.popleft())
'''

def bfs(idx):
    global graph
    global visited
    queue = deque()
    
    visited[idx] = True
    queue.append(idx)
    print(idx, end=' ')
    
    currentIdx = idx
    while queue:
        for i in graph[currentIdx]:
            if not visited[i]:
                visited[i] = True
                print(i, end=' ')
                queue.append(i)
        currentIdx = queue.popleft()
    
    
dfs(1)
print()
visited = [False for _ in range(len(graph))]
bfs(1)
print()

