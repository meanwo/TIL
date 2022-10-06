from collections import deque
import copy

def bfs(y1, x1):
    global arr
    q = deque()
    new_arr = [[0]*W for _ in range(H)]

    q.append((y1, x1))

    while q:

        y, x = q.popleft()
        if arr[y][x] > 1:
            for i in range(4):
                for j in range(1, arr[y][x]):
                    dy = directy[i]*j + y
                    dx = directx[i]*j + x
                    if not (0 <= dy < H and 0 <= dx < W): continue
                    if arr[dy][dx] == 0: continue
                    q.append((dy,dx))
                    # arr[dy][dx] = 0
        arr[y][x] = 0

    # i : 열, j : 행
    for i in range(W):
        idx = H-1
        for j in range(H-1, -1, -1):
            if arr[j][i] != 0:
                new_arr[idx][i] = arr[j][i]
                idx -= 1
    arr = new_arr

def choice_ball(arr):

    loc_list = []
    # print(arr)
    for i in range(W):
        for j in range(H):
            if arr[j][i] != 0:
                loc_list.append((j, i))
                break
    return loc_list

def dfs(level):
    global min_total, arr, min_arr
    if level == N:
        cnt = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j] != 0:
                    cnt += 1
        if cnt < min_total:
            min_total = cnt
            min_arr = copy.deepcopy(arr)
        return

    next_ball = choice_ball(arr)
    # print(next_ball)
    if len(next_ball) == 0:
        min_total = 0
        return
    for i in range(len(next_ball)):
        backup = copy.deepcopy(arr)
        bfs(next_ball[i][0], next_ball[i][1])
        dfs(level+1)
        arr = backup

T = int(input())
for test_case in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    new_arr = [[0]*W for _ in range(H)]
    directy = [1, -1, 0, 0]
    directx = [0, 0, 1, -1]
    min_total =21e8


    dfs(0)
    print(f'#%d %d' %(test_case, min_total))

# 1 4 4
# 0 0 0 0
# 2 0 0 1
# 2 0 0 1
# 1 1 0 1
