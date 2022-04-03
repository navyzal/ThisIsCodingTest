N = int(input())

D = [0] * (N+1)

D[1] = 1
D[2] = 3

for i in range(3, N+1):
    D[i] = (D[i-1] + D[i-2]*2) % 796796
    
print(D[N])

    