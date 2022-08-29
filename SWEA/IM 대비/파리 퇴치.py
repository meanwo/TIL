T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_arr = 0
            for k in range(M):
                for l in range(M):
                    sum_arr += arr[i+k][j+l]
            if sum_arr > max_sum:
                max_sum = sum_arr
    print(f'#%d %d' %(test_case, max_sum))