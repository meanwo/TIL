from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())

visited = [[-1 for _ in range(500001)] for _ in range(2)]
def bfs():
    q = deque()
    q.append([N, 0])
    visited[0][N] = 0
    while q:
        x, cnt = q.popleft()
        flag = cnt % 2

        for dx in [x+1, x-1, x*2]:
            if 0 <= dx <= 500000 and visited[1-flag][dx] == -1:
                visited[1-flag][dx] = cnt+1
                q.append([dx, cnt+1])


bfs()

t = 0
flag = 0
res = -1
while K <= 500000:
    if visited[flag][K] != -1:
        if visited[flag][K] <= t:
            res = t
            break
    flag = 1-flag
    t += 1
    K += t
print(res)