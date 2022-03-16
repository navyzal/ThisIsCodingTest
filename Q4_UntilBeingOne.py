import time

N, K = map(int, input().split())

start = time.time_ns()

count = 0

# 큰 수를 더 효율적으로 처리하기 위해서는 N이 K의 배수가 되도록 한 후 효율적으로 한번에 빼는 방식을 사용
# 결과는 작은 수 대비 245785배 빠르다... -0-;;;;;
'''
100000000000000000000001 35353535
44847997
35000  nano seconds...
'''

while N != 1:
    count += N - (N//K*K)
    N //= K
    if N == 0:
        count -= 1
        break
    else:
        count += 1


# 작은 수..
'''
100000000000000000000001 35353535
44847997
8602473000  nano seconds...
'''

'''
while N != 1:
    if N % K == 0:
        N /= K
        count += 1
    else:
        N -= 1
        count += 1
'''

print(count)

print(time.time_ns() - start, ' nano seconds...')
