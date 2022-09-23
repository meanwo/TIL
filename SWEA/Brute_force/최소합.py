T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    new_arr = [[0]*N for _ in range(N)]
    new_arr[0][0] = arr[0][0]
    for i in range(1, N):
        new_arr[0][i] = new_arr[0][i-1]+arr[0][i]
        new_arr[i][0] = new_arr[i-1][0]+arr[i][0]

    for i in range(1, N):
        for j in range(1, N):
            new_arr[i][j] = min(new_arr[i-1][j], new_arr[i][j-1]) + arr[i][j]
    print(f'#%d %d' %(test_case, new_arr[N-1][N-1]))

