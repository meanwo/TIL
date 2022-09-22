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

# import copy
# arr = [list(input()) for _ in range(4)]
# N = int(input())
#
#
# dx = [0, 0, 0, 1, -1]
# dy = [0, 1, -1, 0, 0]
#
# new_list =[0]*N
# used_arr = [[0]*4 for _ in range(4)]
# max_new_list = [0]*N
# max_total = 0
# cnt = 0
# arr_copy = copy.deepcopy(arr)
#
# def dfs(level, total):
#     global max_total, max_new_list, cnt, arr
#     if level == N:
#         if total > max_total:
#             max_total = total
#             max_new_list = copy.deepcopy(new_list)
#         return
#     backup = copy.deepcopy(arr)
#
#     for i in range(4):
#         for j in range(4):
#             if used_arr[i][j] == 0 and arr[i][j] != '_':
#                 new_list[level] = arr_copy[i][j]
#                 used_arr[i][j] = 1
#                 cnt = 0
#                 for k in range(5):
#                     if 0 <= i+dy[k] <= 3 and 0 <= j+dx[k] <= 3 and arr[i+dy[k]][j+dx[k]] != '_':
#                         cnt += 1
#                         arr[i+dy[k]][j+dx[k]] = '_'
#                 dfs(level+1, total+cnt)
#                 new_list[level] = 0
#                 used_arr[i][j] = 0
#                 arr = copy.deepcopy(backup)
#
# dfs(0, 0)
# max_new_list.sort()
# print(*max_new_list)


# 3번
# N = int(input())
# N_list = list(map(int, input().split()))
#
# cnt = 0
# total_cnt = 0
# def dfs(level, result):
#     global cnt, total_cnt
#     if level == 0:
#         result = N_list[0]
#
#     if level == N-1:
#         total_cnt+= 1
#         # print(total_cnt, result)
#         if result == 100:
#             cnt += 1
#
#         return
#
#
#     backup = result
#
#     dfs(level+1, result**2 - (N_list[level+1])**2)
#     result = backup
#
#     dfs(level+1, max(result, N_list[level+1]))
#     result = backup
#
#     dfs(level+1, result**2 - (N_list[level+1])**2)
#     result = backup
#
#     dfs(level+1, (result+N_list[level+1])**2)
#
# dfs(0, 0)
# print(cnt)

# 4번
# import copy
# N = int(input())
# N_list = list(map(int, input().split()))
# N_list2 = [0]*N
# choose_number_lst = []
# total = 0
# used_list = [0]*N
# max_total = 0
# max_used_list = []
# def dfs(level, start, total):
#     global max_total, N_list2, max_used_list
#     if used_list == [1] * N:
#         if max_total < total:
#
#             max_total = total
#
#             max_used_list = copy.deepcopy(N_list2)
#             # print(max_total)
#             # print(max_used_list)
#         return
#     if level == (N+1)//2:
#         return
#
#     for i in range(start, N):
#         for j in range(-1, 2):
#             if 0 <= i+j < N:
#                 if used_list[i+j] == 0:
#                     used_list[i+j] = 1
#         N_list2[i] = 1
#         dfs(level+1, i+2, total+N_list[i])
#         N_list2[i] = 0
#         for j in range(-1, 2):
#             if 0 <= i + j < N:
#                 if used_list[i + j] == 1:
#                     used_list[i + j] = 0
#
#
#
# dfs(0, 0, 0)
#
# for i in range(N):
#     if max_used_list[i] == 1:
#         choose_number_lst.append(N_list[i])
#
# for i in range(len(choose_number_lst)):
#     if i == len(choose_number_lst)-1:
#         print(f'%d=%d' %(choose_number_lst[i], max_total), end='')
#     else:
#         print(f'%d+' %(choose_number_lst[i]), end='')

# 5번
import copy

def min_except_zero(arr, min_num):
    for i in range(len(arr)):
        if arr[i] != 0 and min_num > arr[i]:
            min_num = arr[i]
    return min_num

arr = list(map(int, input().split()))
level = int(input())
level_init = copy.deepcopy(level)
max_total = 0
def find_total(level, arr, total):
    global max_total
    form = [0, 3, 3, 6, 1, 5]
    if level == 0:
        if total > max_total:
            max_total = total
        return
    final_food = 0
    if level == 1:
        if level_init == 1:
            for i in range(3):
                max_num = max(arr[form[i * 2]:form[i * 2 + 1]])
                final_food += max_num
                arr[arr.index(max_num)] = 0
        else:
            for i in range(6):
                if arr[i] != 0:
                    final_food += arr[i]
        final_food = final_food*2**(level_init-1)
        find_total(level-1, arr, total+final_food)

    else:

        level_sum = 0
        for i in range(3):
            zero_cnt = 0
            for j in range(len(arr)):
                if arr[j] == 0:
                    zero_cnt += 1
            if (level-1)*3 >= 6-zero_cnt:
                min_num = min(arr[form[i*2]:form[i*2+1]])
                level_sum += min_num
                arr[arr.index(min_num)] = 0
            else:
                min_num = min_except_zero(arr[form[i*2]:form[i*2+1]], 999)
                level_sum += min_num
                arr[arr.index(min_num)] = 0

        level_sum = level_sum * 2 ** (level_init - level)
        find_total(level - 1, arr, total+level_sum)

find_total(level, arr, 0)
print(max_total)

# 6번
arr = list(input())
N = int(input())

def cal_score(arr):
    score = 0
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            score -= 50
        elif abs(ord(arr[i])-ord(arr[i+1])) <= 5:
            score += 3
        elif abs(ord(arr[i])-ord(arr[i+1])) >= 20:
            score += 10
    return score
max_score = 0

def dfs(level):
    global max_score
    if level == N:
        score = cal_score(arr)
        if max_score < score:
            max_score = score
        return

    for i in range(len(arr)-1):
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            dfs(level+1)
            arr[i], arr[j] = arr[j], arr[i]


dfs(0)
print(max_score)
