'''
2
홍길동 95
이순신 77
'''
N = int(input())

dic = {}
for _ in range(N):
    name, score = list(input().split())
    dic[name] = int(score)

dic2 = sorted(dic.items(), key=lambda x: x[1])


for i in dic2:
    print(i[0], end=' ')

print()