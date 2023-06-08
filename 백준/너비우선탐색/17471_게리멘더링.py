from itertools import combinations
from collections import deque

N = int(input())
population = list(map(int, input().split()))
near_list = []
for i in range(N):
    near_list.append(list(map(int, input().split()[1:])))
# print(near_list)
N_list = [i+1 for i in range(N)]
N_set = set(N_list)
# print(N_set)
total_list = []
for i in range(1, 1+N//2):
    a_set = list(combinations(N_list, i))
    # print(a_set)
    for j in range(len(a_set)):
        # print(a_set[j])
        b_set = N_set - set(a_set[j])
        total_list.append(list((list(a_set[j]), list(b_set))))

def bfs(g):
    q = deque()
    check = [False for _ in range(N)]
    q.append(g[0])
    check[g[0]-1] = True

    level, count = 1, 0
    while q:
        tmp = q.popleft()
        count += population[tmp-1]
        for i in near_list[tmp-1]:
            if i in g and not check[i-1]:
                check[i-1] = True
                level += 1
                q.append(i)
    if level == len(g):
        return count
    else:
        return False


result = 21e9
for i in range(len(total_list)):
    a_team = total_list[i][0]
    b_team = total_list[i][1]

    a_result = bfs(a_team)
    # print(a_result)
    b_result = bfs(b_team)
    # print(b_result)
    if a_result and b_result:
        result = min(result, abs(a_result - b_result))

if result == 21e9:
    print(-1)
else:
    print(result)



