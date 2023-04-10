import sys
from collections import deque

A, B, N, M = map(int, sys.stdin.readline().split())
used = [0] * 100001
cnt = 0


def bfs(N, M):
    global cnt
    q = deque()
    q.append((N, cnt))
    used[N] = 1
    while q:
        x, cnt = q.popleft()
        if x == M:
            break
        for i in range(8):
            if i == 0:
                dx = x + 1
                if not (0 <= dx <= 100000) or used[dx] == 1: continue
                used[dx] = 1
                q.append((dx, cnt + 1))
            if i == 1:
                dx = x - 1
                if not (0 <= dx <= 100000) or used[dx] == 1: continue
                used[dx] = 1
                q.append((dx, cnt + 1))
            if i == 2:
                dx = x + A
                if not (0 <= dx <= 100000) or used[dx] == 1: continue
                used[dx] = 1
                q.append((dx, cnt + 1))
            if i == 3:
                dx = x - A
                if not (0 <= dx <= 100000) or used[dx] == 1: continue
                used[dx] = 1
                q.append((dx, cnt + 1))
            if i == 4:
                dx = x + B
                if not (0 <= dx <= 100000) or used[dx] == 1: continue
                used[dx] = 1
                q.append((dx, cnt + 1))
            if i == 5:
                dx = x - B
                if not (0 <= dx <= 100000) or used[dx] == 1: continue
                used[dx] = 1
                q.append((dx, cnt + 1))
            if i == 6:
                dx = x * A
                if not (0 <= dx <= 100000) or used[dx] == 1: continue
                used[dx] = 1
                q.append((dx, cnt + 1))
            if i == 7:
                dx = x * B
                if not (0 <= dx <= 100000) or used[dx] == 1: continue
                used[dx] = 1
                q.append((dx, cnt + 1))
    return cnt


result = bfs(N, M)
print(result)
