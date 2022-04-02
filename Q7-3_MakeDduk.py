'''
4 6
19 15 10 17
'''

N, M = map(int, input().split())

arr = list(map(int, input().split()))

result = 0
start = 1
end = max(arr)
cut = 0
mid = 0

while start <= end:
    mid = (start + end) // 2
    
    for i in arr:
        if i > mid:
            result += i - mid

    if result == M:        
        cut = mid
        break
    elif result < M:
        end = mid - 1        
    else:
        start = mid + 1
        cut = mid

    result = 0


print(cut)


