import copy
min_total = 999
def dfs(level, total):
    global min_total, select_list
    if level == N-1:
        total += arr[select_list[-1]][0]
        if total < min_total:
            min_total = total
        return


    for i in range(N):
        if used_list[i] == 1: continue
        used_list[i] = 1
        backup_total = copy.deepcopy(total)
        backup = copy.deepcopy(select_list)
        a = select_list[-1]
        select_list.append(i)
        b = select_list[-1]
        dfs(level+1, total+arr[a][b])
        select_list = backup
        total = backup_total
        used_list[i] = 0

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used_list = [0]*N
    select_list = [0]
    used_list[0] = 1
    min_total = 999
    dfs(0, 0)
    print(f'#%d %d' %(test_case, min_total))



