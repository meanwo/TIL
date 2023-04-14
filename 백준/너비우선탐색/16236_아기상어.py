from collections import deque
import sys
from copy import deepcopy
N = int(sys.stdin.readline())

arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

directy = [-1, 0, 0, 1]
directx = [0, -1, 1, 0]


def find_shark():
    y, x = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                y, x = i, j
    return y, x



def bfs(y1, x1, level):
    global arr
    q = deque()
    # 첫 상어의 위치를 q에 추가
    q.append([y1, x1])
    used = [[0] * N for _ in range(N)]
    used[y1][x1] = 1
    eat_able = deque()
    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if not (0 <= dy < N and 0 <= dx < N): continue
            if used[dy][dx] != 0: continue
            if arr[dy][dx] == 0 or arr[dy][dx] <= level:
                used[dy][dx] = used[y][x]+1
                if arr[dy][dx] < level and arr[dy][dx] != 0:
                    q.append([dy, dx])
                    eat_able.append([used[dy][dx]-1, dy, dx])
                elif arr[dy][dx] in [level, 0]:
                    q.append([dy, dx])

    eat_able = sorted(eat_able, key=lambda x: (x[0], x[1], x[2]))
    if eat_able:
        return eat_able[0]
    else:
        return -1


total_dist = 0
y1, x1 = find_shark()
level = 2
eat = 0
while bfs(y1, x1, level) != -1:
    total_dist += bfs(y1, x1, level)[0]
    arr[y1][x1] = 0
    y1, x1 = [bfs(y1, x1, level)[1], bfs(y1, x1, level)[2]]
    eat += 1
    if eat == level:
        level += 1
        eat = 0
print(total_dist)
