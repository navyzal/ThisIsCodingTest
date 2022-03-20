import time

start = time.time_ns()
N = int(input())

count = 0

'''
5
3
11475
1076521000  nano seconds ...

for h in range(N+1):
    if '3' in str(h):
        print(h)
        count += 60*60
        continue
    for m in range(60):
        if '3' in str(m):
            count += 60
            continue
        for s in range(60):
            if '3' in str(s):
                count += 1
                continue
'''

# data 숫자가 많지 않아 굳이 위와 같이 복잡하게 가지치기를 할 필요가 없다..... 단순히 짜자..
'''
5
11475
1273298000  nano seconds ...
'''
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1                

print(count)
print(time.time_ns() - start, " nano seconds ...")
