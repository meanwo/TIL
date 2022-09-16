import copy
# 1번
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
#
# arr_copy = copy.deepcopy(arr)
#
# max_total = 0
#
# def get_score(arr):
#     get_sum = 1
#     for i in range(n):
#         col_sum = 0
#         for j in range(n):
#             col_sum += arr[j][i]
#         get_sum *= col_sum
#     return get_sum
#
# def dfs(level, total):
#     global max_total
#     if level == n:
#         print(arr)
#         # total = get_score(arr)
#         if total > max_total:
#             max_total = total
#         return
#     for i in range(n):
#         # backup = total
#         for j in range(n):
#             arr[level][j] = arr_copy[level][(i+j+1) % n]
#             # arr[level][j] = arr_copy[level][(j+n-1) % n]
#             total = get_score(arr)
#         # print(arr)
#         dfs(level+1, total)
#         # total = backup
#
# dfs(0, 0)
# print(f'%d점' %max_total)


# 2번

import copy
arr = [list(input()) for _ in range(4)]
N = int(input())


dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]

new_list =[0]*N
used_arr = [[0]*4 for _ in range(4)]
max_new_list = [0]*N
max_total = 0
cnt = 0
arr_copy = copy.deepcopy(arr)

def dfs(level, total):
    global max_total, max_new_list, cnt
    if level == N:
        print(new_list)
        print(max_new_list)
        if total > max_total:
            max_total = total
            max_new_list = copy.deepcopy(new_list)
        return
    for i in range(4):
        for j in range(4):
            backup = total
            if used_arr[i][j] == 0 and arr[i][j] != '_':
                new_list[level] = arr_copy[i][j]
                # new_list[level] = arr_copy[i][j]
                used_arr[i][j] = 1
                cnt = 0
                for k in range(5):
                    if 0 <= i+dy[k] <= 3 and 0 <= j+dx[k] <= 3 and arr[i+dy[k]][j+dx[k]] != '_':
                        cnt += 1
                        arr[i+dy[k]][j+dx[k]] = '_'
                dfs(level+1, total+cnt)
                new_list[level] = 0
                used_arr[i][j] = 0
                total = backup


            # if arr[i][j].isalpha() and used_arr[i][j] == 0:
            #     new_list[level] = arr[i][j]
            #     used_arr[i][j] = 1
            #     cnt = 0
            #
            #     for k in range(5):
            #         if 0 <= i+dy[k] <= 3 and 0 <= j+dx[k] <= 3:
            #             if arr[i+dy[k]][j+dx[k]].isalpha():
            #                 cnt += 1
            #                 arr[i+dy[k]][j+dx[k]] = '_'
            #     dfs(level+1, total+cnt)
            #     # total = backup
            #     new_list[level] = 0
            #     used_arr[i][j] = 0


dfs(0, 0)
print(max_total)
print(max_new_list)

# 3번

