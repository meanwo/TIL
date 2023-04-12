from collections import deque
import sys
from copy import deepcopy
R, C = map(int, sys.stdin.readline().split())
used = [[-1]*C for _ in range(R)]
used_fire = [[-1]*C for _ in range(R)]

maze = []
for i in range(R):
    maze.append(list(sys.stdin.readline().rstrip()))



directy = [1, -1, 0, 0]
directx = [0, 0, 1, -1]


def bfs():
    global maze
    fire_q = deque()
    jh_q = deque()
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'F':
                fire_q.append([i, j])
                used_fire[i][j] = 0
            elif maze[i][j] == 'J':
                jh_q.append([i, j])
                used[i][j] = 0
    while fire_q:
        y, x = fire_q.popleft()
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if not (0 <= dy < R and 0 <= dx < C): continue
            if used_fire[dy][dx] != -1: continue
            if maze[dy][dx] == '#': continue
            used_fire[dy][dx] = used_fire[y][x]+1
            fire_q.append([dy,dx])


    while jh_q:
        y, x = jh_q.popleft()
        if y in [0, R-1] or x in [0, C-1]:
            return used[y][x]+1

        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if not (0 <= dy < R and 0 <= dx < C): continue
            if maze[dy][dx] != '.' or used[dy][dx] != -1: continue
            used[dy][dx] = used[y][x] + 1
            if used_fire[dy][dx] > used[dy][dx] or used_fire[dy][dx] == -1:
                jh_q.append([dy, dx])

    return "IMPOSSIBLE"


print(bfs())