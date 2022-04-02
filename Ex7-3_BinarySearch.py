'''
10 7
1 3 5 7 9 11 13 15 17 19
#4

10 7
1 3 5 6 9 11 13 15 17 19
#Not found
'''


N, K = map(int, input().split())
Arr = list(map(int, input().split()))

def BinarySearchR(start, end):
    global N, K, Arr
    
    if start > end:
        return None
    
    mid = (start + end) //2

    if K == Arr[mid]:        
        return mid
    elif K < Arr[mid]:
        return BinarySearchR(start, mid-1)
    # K > Arr[mid]:
    else:
        return BinarySearchR(mid+1, end)

def BinarySearch(start, end):
    global N, K, Arr
    
    while start <= end:
        mid = (start + end) // 2
        
        if Arr[mid] == K:
            return mid
        elif K < Arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

        
found = BinarySearch(0, N-1)
if found:
    print(found+1)
else:
    print('Not found')