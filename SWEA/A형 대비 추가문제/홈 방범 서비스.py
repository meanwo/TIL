T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total_home_cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                total_home_cnt += 1

    max_profit = M * total_home_cnt
    # print(max_profit)
    K = 1
    over_cost = 1
    while max_profit > over_cost:
        K += 1
        over_cost = 2 * K ** 2 - 2 * K + 1
    # print(over_cost)
    # print(K)

    flag = 0
    K -= 1
    for a in range(K, -1, -1):
        cost = 2 * a ** 2 - 2 * a + 1
        # print(cost)
        max_home_cnt = 0
        for i in range(N):
            for j in range(N):
                home_cnt = 0
                able_list = []
                for k in range(-(a - 1), a):
                    for l in range(-(a - abs(k) - 1), a - abs(k)):
                        if not (0 <= i + k < N and 0 <= j + l < N): continue
                        able_list.append((i + k, j + l))
                        if arr[i + k][j + l] == 1:
                            home_cnt += 1
                if home_cnt * M >= cost:
                    max_home_cnt = max(home_cnt, max_home_cnt)
        if max_home_cnt * M >= cost:
            print(f'#%d %d' % (test_case, max_home_cnt))
            break