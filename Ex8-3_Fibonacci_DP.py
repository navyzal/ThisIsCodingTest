import time

N = int(input())

start = time.time()
DP_Node = [0] * (N+1)

DP_Node[1] = 1
DP_Node[2] = 1

for i in range(3, N+1):
    DP_Node[i] = DP_Node[i-2] + DP_Node[i-1]

print(DP_Node[N])

print(f'{time.time() - start} secods....')

'''
Use Recursive..
40
102334155
19.939693927764893 secods....

Use Memorization...
40
102334155
7.176399230957031e-05 secods....

Use BottomUp DP...
40
102334155
5.888938903808594e-05 secods....
'''