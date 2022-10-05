from collections import deque
# 폭탄 경로 문제
N, W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]


# 새 배열에 벽:3 을 최신화
new_arr = [[0]*W for _ in range(H)]
for i in range(5):
    for j in range(5):
        if arr[i][j] == 3:
            new_arr[i][j] = 3


directx = [1, -1, 0, 0]
directy = [0, 0, 1, -1]

def bfs(y1, x1):
    queue = deque()
    for i in range(4):
        queue.append((y1, x1, i))
    new_arr[y1][x1] = 1
    while queue:
        y, x, dir = queue.popleft()
        dy = directy[dir] + y
        dx = directx[dir] + x
        if not(0 <= dx < 5 and 0<= dy < 5): continue
        if arr[dy][dx] == 3: continue
        new_arr[dy][dx] = 1
        queue.append((dy,dx, dir))

for i in range(5):
    for j in range(5):
        if arr[i][j] == 1:
            bfs(i,j)

cnt = 0
for i in range(5):
    for j in range(5):
        if new_arr[i][j] == 0:
            cnt += 1
print(cnt)