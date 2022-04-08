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


INF = int(1e9)

# 노드 수 n, 간선수 m
n, m = map(int, input().split())

# 시작 노드
start = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

# 노드, 연결될 타 노드, 비용
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    
    # 우선 순위 큐에 비용 / 이동할 노드 순서로 넣어서 비용을 기준으로 pop 되게 넣는다.
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        for i in graph[now]:
            # 현재 
            cost = dist + i[1]
            if cost < distance[i[0]]:
                heapq.heappush(q, (cost, i[0]))
                distance[i[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    print(distance[i])
