from pickle import TRUE


# n개를 받아 가장 큰 수는 m번까지 더할 수 있고, 총 k 번 더해서 가장 큰수..
n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort(reverse=True)
first = data[0]
second = data[1]

sum = 0

'''
# 단순 버전
while True:
    for i in range(k):
        if m == 0:
            break
        sum += first
        m -= 1
    if m == 0:
        break
    else:
        sum += second
        m -= 1
'''

# 효율화
pSum = first * k + second

sum = pSum * (m // (k+1)) + first * (m % (k+1))

print(sum)