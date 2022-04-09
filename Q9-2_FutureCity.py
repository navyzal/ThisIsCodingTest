'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''

import heapq


INF = int(1e9)

# 회사 개수 N, 경로 개수 M
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    departure, destination = map(int, input().split())
    graph[departure].append(destination)
    graph[destination].append(departure)

# 방문할 회사의 노드 번호 X, 소개팅 상대 노드 번호 K
x, k = map(int, input().split())

# 목표는 K 를 들렸다가 최종적으로 X 를 가는 가장 빠른 비용 구하기

'''
print(n, m)

print(x, k)
'''
print(graph)

distanceK = [INF] * (n+1)
distanceX = [INF] * (n+1)

def dijikstra(start, distance):    
    q = []
    
    # (비용, 노드) 우선순위 큐 사용
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        for i in graph[now]:            
            cost = 1 + dist            
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

dijikstra(1, distanceK)
dijikstra(k, distanceX)

print(distanceK)
print(distanceX)

print(distanceK[k] + distanceX[x])