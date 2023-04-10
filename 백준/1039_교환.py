from itertools import combinations
from copy import deepcopy
N, M = input().split()
N = list(N)
M = int(M)

max_num = 0
k = [i for i in range(len(N))]
change = list(combinations(k, 2))
print(change)
used = [[] for _ in range(M)]
def dfs(level, N):
    global max_num, change, used
    if level == M:
        max_num = max(max_num, int(''.join(N)))
        return
    for i in range(len(change)):
        if N[change[i][1]] == '0' and change[i][0] == 0: continue
        N_backup = deepcopy(N)
        # print(N, 'before')
        N[change[i][0]], N[change[i][1]] = N[change[i][1]], N[change[i][0]]
        # print(N, 'after')
        if ''.join(N) not in used[level]:
            n2 = ''.join(N)
            # used_backup = deepcopy(used)
            used[level].append(n2)
            print(used)
            dfs(level+1, N)
            # used = used_backup
            N = N_backup
        else:
            N = N_backup

dfs(0, N)
if max_num == 0 or len(N) == 1:
    print(-1)
else:
    print(max_num)
