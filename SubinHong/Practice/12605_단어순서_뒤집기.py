from collections import deque
N = int(input())
li = deque()
for i in range(N):
    li = str(input()).split()
    li.reverse()
    print(f'Case #{i+1}:', ' '.join(li))
    li.clear()
