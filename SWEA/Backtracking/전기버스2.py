def backtracking(level, fuel, cnt):
    global min_cnt

    if cnt > min_cnt:
        return

    if level >= N-1:
        if cnt < min_cnt:
            min_cnt = cnt
        return


    for i in range(info[level], 0, -1):
        backtracking(level+i, fuel-i+info[i], cnt+1)

T = int(input())
for test_case in range(1, T+1):
    A = list(map(int, input().split()))
    N = A[0]
    info = A[1:]

    min_cnt = 999

    backtracking(0, info[0], -1)
    print(f'#%d %d' %(test_case, min_cnt))