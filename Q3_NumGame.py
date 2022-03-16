N, M = map(int, input().split())

largest = 0

for i in range(N):
    data = list(map(int, input().split()))
    if largest < min(data):
        largest = min(data)

print(largest)