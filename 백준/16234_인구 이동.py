import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
A = []
directx = [1, -1, 0, 0]
directy = [0, 0, 1, -1]
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))


def bfs(y1, x1, union):
    global flag
    q = deque()
    q.append([A[y1][x1], y1, x1])
    unionsum = A[y1][x1]
    used[y1][x1] = 1
    while q:

        cntry, y, x = q.popleft()
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if not (0 <= dy < N and 0 <= dx < N): continue
            if used[dy][dx] == 1: continue
            if L <= abs(A[dy][dx] - A[y][x]) <= R:
                flag = 1
                used[dy][dx] = 1
                unionsum += A[dy][dx]

                union.append([dy, dx])
                q.append([A[dy][dx], dy, dx])
    for i in range(len(union)):
        A[union[i][0]][union[i][1]] = unionsum // len(union)
    # print(unionsum)
    # print(union)
    # print(A)





cnt = 0

while True:
    flag = 0
    used = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if used[i][j] == 0:
                bfs(i, j, [[i, j]])

    cnt += 1
    if flag == 0:
        break
print(cnt-1)
