'''
3 2 1
1 2 4
1 3 2
'''
import heapq


INF = int(1e9)

# 도시 개수 N, 통로 개수 M, 메세지 보내고자 하는 도시 노드 번호 C
N, M, C = map(int, input().split())

graph = [[] for i in range(N+1)]

# 통로 정보. X -> Y, 비용 Z
for i in range(M):
    X, Y, Z = map(int, input().split())
    graph[X].append((Y, Z))

distance = [INF] * (N+1)

longest = 0
count = 0

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        for i in graph[now]:
            cost = i[1] + dist
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)

for i in distance:
    if i != INF and i != 0:
        count += 1
        longest = max(longest, i)

print(count, longest)
print(distance)