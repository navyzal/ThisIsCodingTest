'''
2 15
2
3


3 4
3
5
7
'''
N, M = map(int, input().split())

C = []
P = [0] * (M+1)

for _ in range(N):
    t = int(input())
    if t > M:
        continue
    C.append(t)    
    P[t] = 1
    
for i in range(1, M+1):
    for c in C:
        if (i + c) > M:            
            continue
    
        if P[i+c] != 0:
            P[i+c] = min(P[i+c], P[i]+1)
        

print(P)
if P[M] == 0:
    print(-1)
else:
    print(P[M])