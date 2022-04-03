import time
import sys

sys.setrecursionlimit(10000)

N = int(input())
Memory = [0] * N
def fibonacci(num):
    if num == 1 or num == 2:
        return 1
    if Memory[num-1] == 0:
        Memory[num-1] = fibonacci(num-1)
    
    if Memory[num-2] == 0:
        Memory[num-2] = fibonacci(num-2)
    
    return Memory[num-1] + Memory[num-2]


start = time.time()
print(fibonacci(N))
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
'''