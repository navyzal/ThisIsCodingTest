'''
5 3
1 2 5 4 3
5 5 6 6 5
'''

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()   
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i] = B[i]
        print(A)
    else:
        break

print(sum(A))
