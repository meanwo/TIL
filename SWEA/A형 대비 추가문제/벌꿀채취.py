import copy

# honey : 채취할 수 있는 꿀의 한도
def find_max(total, y1, x1, idx, honey):
    global max_total

    if idx == M:
        if max_total < total:
            max_total = total
        return
    # 현재 인덱스의 꿀의 양이 한도를 초과하면 다음번 인덱스로 이동
    if honey < arr[y1][x1]:
        find_max(total, y1, x1+1, idx+1, honey)
    else:
        backup_honey = honey
        backup_total = copy.deepcopy(total)
        # 1: 꿀을 채취할 수 있을 때 채취하는 경우
        honey -= arr[y1][x1]
        total += arr[y1][x1]**2
        find_max(total, y1, x1+1, idx+1, honey)
        # 2: 꿀을 채취할 수 있음에도 다음 번 인덱스로 넘어가는 경우
        honey = backup_honey
        total = backup_total
        find_max(total, y1, x1+1, idx+1, honey)

# print(square_arr)


def dfs(level, starty, result):
    global max_result, used
    if level == 2:
        # print(result)
        # print(used)
        if max_result < result:
            max_result = result
        return

    for i in range(starty, N):
        for j in range(N-M+1):

            backup = copy.deepcopy(result)
            backup_used = copy.deepcopy(used)
            # M의 크기에 따라 같은 행 안에서 건너뛰어야 할 길이가 정해짐.
            if used[i][j] == 0:
                for k in range(-M+1, M):
                    if not (0 <= j+k < N-M+1): continue
                    used[i][j+k] = 1

                dfs(level+1, i, result+square_arr[i][j])
                result = backup
                used = backup_used

T = int(input())
for test_case in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # max_result : 최종 결과값
    max_result = 0
    # N과 M에 의해 정해지는 최대수익 배열
    square_arr = [[0]*(N-M+1) for _ in range(N)]

    used = [[0]*(N-M+1) for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            max_total = 0

            # 벌통 M개 즉, arr[i][j:j+M] 을 선택했을 때 얻을 수 있는 최대 꿀의 양
            find_max(0, i, j, 0, C)
            square_arr[i][j] = max_total

    # print(square_arr)

    dfs(0, 0, 0)
    print(f'#%d %d' %(test_case, max_result))


