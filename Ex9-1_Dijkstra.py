'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

결과:
0
2
3
1
2
4

'''

import heapq


INF=int(1e9)

# 노드 수, 간선 수 입력
n, m = map(int, input().split())

# 시작 노드 입력 받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]

# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))
    
def dijkstra(start):
    q = []
    
    # 시작노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    # heapq 의 heappush 는 비용, 이동할 노드 순서로 넣는다.
    # heapq 와 같은 우선순위 큐는 첫번째 파라미터인 비용을 기준으로 가장 낮은 값 부터 pop 이 되게 된다...
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:    # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        # i -> (연결된 다른 노드, 비용)
        for i in graph[now]:
            cost = dist + i[1]
            
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):    
    # 도달할 수 없는 경우, 무한(Infinity) 라고 출력
    if distance[i] == INF:
        print('Infinity')
    else:
        print(distance[i])
        

        

        
    


