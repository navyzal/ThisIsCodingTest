'''
4
1 3 1 5
'''

N = int(input())
K = list(map(int, input().split()))

D = [0] * 1000
D[0] = K[0]
D[1] = K[1]
D[2] = K[0] + K[2]


for i in range(3, N):
    D[i] = max(D[i-2] + K[i], D[i-3] + K[i])

print(D[N-1])
    