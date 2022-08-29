
def bfs(st_y, st_x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = [[st_y, st_x]]
    visited[st_y][st_x] = 1

    while queue:
        y, x = queue.pop(0)
        if arr[y][x] == 3:
            return distance[y][x] -1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<= ny < N and 0 <= nx < N and arr[ny][nx] != 1 and visited[ny][nx] == 0:
                queue.append([ny, nx])
                visited[ny][nx] = 1
                distance[ny][nx] = distance[y][x] + 1
    return 0

T = int(input())
for i in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    distance = [[0]*N for _ in range(N)]

    for j in range(N):
        for k in range(N):
            if arr[j][k] == 2:
                st_x, st_y = k, j
    result = bfs(st_y, st_x)
    print(f'#%d %d' %(i+1, result))