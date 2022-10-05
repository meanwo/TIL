directy = [1, -1, 0, 0]
directx = [0, 0, 1, -1]
def bfs(y1, x1):
    # 방어탑의 좌표를 입력받았을 때 queue에 방어탑 상하좌우 좌표를 추가
    queue = [(y1, x1, 0), (y1, x1, 1), (y1, x1, 2), (y1, x1, 3)]
    while queue:
        y, x, dir = queue.pop(0)

        dy = directy[dir]+y
        dx = directx[dir]+x
        # 방어탑의 공격이 지도를 벗어나는 경우를 제외
        if not (0 <= dy < N and 0 <= dx < N): continue
        # 방어탑의 공격이 장애물을 만나면 그 방향으로 진행 멈춤
        if arr[dy][dx] == 1: continue
        # (dy, dx) 좌표에 방어탑 공격이 가능하면 new_arr[dy][dx]에 1 저장
        new_arr[dy][dx] = 1
        # 해당 방향으로 더 공격이 가능한지 확인하게 위해 queue에 추가
        queue.append((dy, dx, dir))

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # new_arr 에는 안전지역을 0으로 표시, 나머지 지역은 1을 표시.
    new_arr = [[0]*N for _ in range(N)]


    for i in range(N):
        for j in range(N):
            # 방어탑이 있는 곳은 안전지역에서 제외
            if arr[i][j] == 2:
                new_arr[i][j] = 1
                bfs(i, j)
            # 장애물이 있는 곳은 안전지역에서 제외
            elif arr[i][j] == 1:
                new_arr[i][j] = 1

    cnt = 0
    for i in range(N):
        for j in range(N):
            # new_arr 에서 0의 개수 = 안전지역의 개수
            if new_arr[i][j] == 0:
                cnt += 1

    print(f'#%d %d' %(test_case, cnt))