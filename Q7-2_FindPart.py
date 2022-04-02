'''
5
8 3 7 9 2
3
5 7 9
'''
N = int(input())
Stock = list(map(int, input().split()))
Stock.sort()

M = int(input())
Order = list(map(int, input().split()))
Order.sort()


'''
print(N, M)
print(Stock)
print(Order)
'''

for item in Order:
    if item in Stock:
        print('yes', end=' ')
    else:
        print('no', end=' ')
print()
