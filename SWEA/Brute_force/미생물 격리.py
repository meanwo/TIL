T = int(input())

for test_case in range(1, T+1):

    directx = [0, 0, -1, 1]
    directy = [-1, 1, 0, 0]
    N, M, K = map(int, input().split())
    arr = [[[0, 0]]*N for _ in range(N)]
    next_arr = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(K):
        y, x, count, dir = map(int, input().split())
        arr[y][x] = [count, dir]

    for i in range(M):

        next_arr = [[[] for _ in range(N)] for _ in range(N)]

        for j in range(N):
            for k in range(N):
                # 위쪽 방향
                if arr[j][k][1] == 1:
                    if j == 1:
                        next_arr[j-1][k].append([arr[j][k][0]//2, 2])
                    else:
                        next_arr[j-1][k].append(arr[j][k])

                # 아래쪽 방향
                if arr[j][k][1] == 2:
                    if j == N-2:
                        next_arr[j+1][k].append([arr[j][k][0]//2, 1])
                    else:
                        next_arr[j+1][k].append(arr[j][k])

                # 왼쪽 방향
                if arr[j][k][1] == 3:
                    if k == 1:
                        next_arr[j][k-1].append([arr[j][k][0]//2, 4])
                    else:
                        next_arr[j][k-1].append(arr[j][k])
                # 오른쪽 방향
                if arr[j][k][1] == 4:
                    if k == N-2:
                        next_arr[j][k+1].append([arr[j][k][0]//2, 3])
                    else:
                        next_arr[j][k+1].append(arr[j][k])

        for j in range(N):
            for k in range(N):
                if len(next_arr[j][k]) != 0:
                    new_dir = max(next_arr[j][k])[1]
                    part_total = 0
                    for l in range(len(next_arr[j][k])):
                        part_total += next_arr[j][k][l][0]
                    arr[j][k] = [part_total, new_dir]
                else:
                    arr[j][k] = [0, 0]

    total = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j][0] != 0:
                total += arr[i][j][0]
    print(f'#%d %d' %(test_case, total))
