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


4 2
1 3
2 4
3 4
'''

INF = int(1e9)

# 회사 개수 N, 경로 개수 M
n, m = map(int, input().split())

graph = [([INF] * (n+1)) for _ in range(n+1)]

for i in range(m):
    departure, destination = map(int, input().split())
    graph[departure][destination] = 1
    graph[destination][departure] = 1

# 방문할 회사의 노드 번호 X, 소개팅 상대 노드 번호 K
x, k = map(int, input().split())

for i in range(n+1):
    graph[i][i] = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            graph[j][i] = graph[i][j]

result = graph[1][k] + graph[k][x]
print(result if result < INF else -1)
