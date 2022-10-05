from collections import deque
import copy
def dfs(a_food, level, start):
    global Min

    if level == N/2:
        # b_food = list(set(i for i in range(N))-set(a_food))
        # a_food_copy = copy.deepcopy(a_food)
        # a_list.append(a_food_copy)
        # if b_food in a_list:
        #     return
        b_food = []
        for i in range(N):
            if check[i] == 0:
                b_food.append(i)
        a_total = 0
        b_total = 0
        for j in range(len(b_food)-1):
            for k in range(j+1, N//2):
                a_total += arr[a_food[j]][a_food[k]] + arr[a_food[k]][a_food[j]]
                b_total += arr[b_food[j]][b_food[k]] + arr[b_food[k]][b_food[j]]
        # for j in range(len(a_food)-1):
        #     for k in range(j+1, N//2):
        #         a_total += arr[a_food[j]][a_food[k]] + arr[a_food[k]][a_food[j]]

        gap = abs(a_total - b_total)
        Min = min(Min, gap)
        return

    for i in range(start, N):
        if check[i] == 0:
            check[i] = 1
            a_food.append(i)
            dfs(a_food, level+1, i+1)
            check[i] = 0
            a_food.pop()

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    a_food = deque()
    a_list = deque()
    check = [0]*N
    Min = 21e8
    dfs([], 0, 0) # a_food, level, start
    print(f'#%d %d' %(test_case, Min))