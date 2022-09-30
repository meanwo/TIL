def bfs(x1, y1):
    queue = [(y1, x1)]
    while queue:

        y, x = queue.pop(0)
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x

            if not(0 <= dx < N and 0 <= dy < N): continue
            plus_fuel = 0
            if arr[dy][dx] > arr[y][x]:
                plus_fuel = arr[dy][dx] - arr[y][x]
            if new_arr[dy][dx] > new_arr[y][x] + plus_fuel + 1:
                new_arr[dy][dx] = new_arr[y][x] + plus_fuel + 1
                queue.append((dy, dx))



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    new_arr = [[99999999]*N for _ in range(N)]
    new_arr[0][0] = 0
    directx = [1, -1, 0, 0]
    directy = [0, 0, 1, -1]


    bfs(0, 0)

    print(f'#%d %d' %(test_case, new_arr[N-1][N-1]))



