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
N = list(map(int, input().split()))
turn = int(input())
turn_init = copy.deepcopy(turn)
# used_list = [0]*6
max_total = 0
def dfs(turn, total):
    global max_total
    if turn == 0:
        if total > max_total:
            max_total = total
        return

    if turn == 1:
        print(N)
        final_food = 0
        for i in range(6):
            if N[i] != 0:
                final_food += N[i]
        print(final_food)
        total += final_food*2**(turn_init-1)
        # backup = total
        # max_1 = max(N[0:3])
        # N[N.index(max_1)] = 0
        # max_2 = max(N[3:6])
        # N[N.index(max_2)] = 0
        # max_3 = max(N[1:5])
        # N[N.index(max_3)] = 0
        # total += (max_1+max_2+max_3)*2**(turn_init-1)
        # print(total)
        dfs(turn-1, total)
        # total = backup
    else:
        if turn == turn_init:
            min_list = min_total(N, 999)
            for i in range(6):
                if min_list[i] == 1:
                    total += N[i]
                    N[i] = 0
            dfs(turn-1, total)
        else:
            dfs(turn-1, total)


        # # backup = total
        # min_1 = min_except_zero(N[0:3], 999)
        # # min_1 = min(N[0:3])
        # N[N.index(min_1)] = 0
        # min_2 = min_except_zero(N[3:6], 999)
        # # min_2 = min(N[3:6])
        # N[N.index(min_2)] = 0
        # min_3 = min_except_zero(N[1:5], 999)
        # # min_3 = min(N[1:5])
        # N[N.index(min_3)] = 0
        # total += (min_1 + min_2 + min_3)*(turn_init-turn+1)
        # print(total)
        # dfs(turn - 1, total)



def min_except_zero(arr, min_num):
    for i in range(len(arr)):
        if arr[i] != 0 and min_num > arr[i]:
            min_num = arr[i]
    return min_num

def find_total(arr):
    total = 0
    for i in range(0, 3):
        total += arr[i]
        arr[i] = 0
        for j in range(3, 6):
            total += arr[j]
            arr[j] = 0
            for k in range(1, 5):
                total += arr[k]
    return arr, total
result = find_total(N)
print(result[1])
def min_total(arr, min_num):
    used_list = [0]*6
    for i in range(0, 3):
        used_list[i] = 1
        for j in range(3, 6):
            if used_list[j] == 0:
                used_list[j] = 1
                for k in range(1, 5):
                    total = 0
                    if used_list[k] == 0:
                        used_list[k] = 1
                        total += arr[i]+arr[j]+arr[k]
                        if min_num > total:
                            min_num = total
                            min_used_list = copy.deepcopy(used_list)
                        used_list[k] = 0
                used_list[j] = 0
        used_list[i] = 0
    return min_used_list

def min_total2(arr, min_num):
    used_list = [0]*6
    for i in range(0, 3):
        used_list[i] = 1
        for j in range(3, 6):
            # if used_list[j] == 0:
            used_list[j] = 1
            for k in range(1, 5):
                total = 0
                    # if used_list[k] == 0:
                used_list[k] = 1
                total += arr[i]+arr[j]+arr[k]
                if min_num > total:
                    min_num = total
                    min_used_list = copy.deepcopy(used_list)
                    used_list[k] = 0
                used_list[j] = 0
        used_list[i] = 0
    return min_used_list
# dfs(turn, 0)
# print(max_total)

# result = min_total(N, 999)
# print(result)