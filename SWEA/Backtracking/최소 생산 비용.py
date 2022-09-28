def backtracking(level, s):
    global min_sum
    if level == N:
        if s < min_sum:
            min_sum = s
        return
    #백트래킹 구문
    elif level != N:
        if s >= min_sum:
            return

    for i in range(N):
        if used_list[i] == 0:
            used_list[i] = 1
            backtracking(level+1, s+arr[level][i])
            used_list[i] = 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used_list = [0]*N

    min_sum = 999
    backtracking(0, 0)
    print(f'#%d %d' %(test_case, min_sum))
