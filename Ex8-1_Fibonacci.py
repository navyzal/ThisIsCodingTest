import time

N = int(input())

def fibonacci(num):
    if num == 1 or num == 2:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)


start = time.time()
print(fibonacci(N))
print(f'{time.time() - start} secods....')

'''
40
102334155
19.939693927764893 secods....
'''