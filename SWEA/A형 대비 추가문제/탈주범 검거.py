from collections import deque

direct = [
    [(0, 0)],
    [(-1, 0), (1, 0), (0, 1), (0, -1)],
    [(1, 0), (-1, 0)],
    [(0, -1), (0, 1)],
    [(-1, 0), (0, 1)],
    [(1, 0), (0, 1)],
    [(1, 0), (0, -1)],
    [(-1, 0), (0, -1)]
]

def bfs(y1, x1, L):
    global cnt
    cnt = 0
    q = deque()
    q.append((y1, x1, L))
    used[y1][x1] = 1
    while q:
        y, x, time = q.popleft()
        cnt += 1
        if arr[y][x] != 0:
            for i in range(len(direct[arr[y][x]])):
                dy = y+direct[arr[y][x]][i][0]
                dx = x+direct[arr[y][x]][i][1]
                if not (0 <= dy < N and 0 <= dx < M): continue
                if used[dy][dx] == 1: continue
                for j in range(len(direct[arr[dy][dx]])):
                    dy2 = dy+direct[arr[dy][dx]][j][0]
                    dx2 = dx+direct[arr[dy][dx]][j][1]
                    if not (0 <= dy2 < N and 0 <= dx2 < M): continue
                    if dy2 == y and dx2 == x and time > 1:
                        used[dy][dx] = 1
                        q.append((dy, dx, time-1))
                        break



T = int(input())
for test_case in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [[0]*M for _ in range(N)]
    bfs(R, C, L)
    print(f'#%d %d' %(test_case, cnt))