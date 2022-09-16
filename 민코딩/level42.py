# 1번
# arr = list(input())
# new_list = [0]*3
#
# def dfs(level, start):
#     if level == 3:
#         for i in range(3):
#             print(new_list[i], end='')
#         print()
#         return
#     for i in range(start, len(arr)):
#         new_list[level] = arr[i]
#         dfs(level+1, i)
#
# dfs(0, 0)

# 2번
# arr = list(map(int, input().split()))
# max_result = 0
# min_result = 9999
# new_list = [0]*5
# used_list = [0]*5
#
# def dfs(level):
#     global max_result, min_result
#     if level == 5:
#         result = find_result(new_list)
#         if max_result < result:
#             max_result = result
#         if min_result > result:
#             min_result = result
#
#     for i in range(5):
#         if used_list[i] == 0:
#             used_list[i] = 1
#             new_list[level] = arr[i]
#             dfs(level+1)
#             used_list[i] = 0
#
# def find_result(lst):
#     result = lst[0]*lst[1] - lst[2]*lst[3] + lst[4]
#     return result
#
#
# dfs(0)
# print(max_result)
# print(min_result)

# 3번
# arr = ['BTS', 'SBS', 'BS', 'CBS', 'SES']
# sentence = input()
#
# min_cnt = 999
# def dfs(level, result, cnt):
#     global min_cnt
#     if len(result) >= len(sentence):
#         if min_cnt > cnt:
#             min_cnt = cnt
#         return
#     for i in range(5):
#         backup = result
#         dfs(level+1, result+arr[i], cnt+1)
#         result = backup
#
# dfs(0, '', 0)
# print(min_cnt)

# 4번
# coin_list = [10, 40, 60]
# change = int(input())
# min_cnt = 9999
# def dfs(level, change, cnt):
#     global coin_list, min_cnt
#     if change <= 0:
#         if cnt < min_cnt:
#             min_cnt = cnt
#         return
#
#     for i in range(len(coin_list)):
#         backup = change
#         dfs(level+1, change-coin_list[i], cnt+1)
#         change = backup
#
# dfs(0, change, 0)
# print(min_cnt)

# 5번
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# N = int(input())
#
# cnt = 0
# def dfs(level, total):
#     global cnt
#     if level == N:
#         if total == 10:
#             cnt += 1
#         return
#
#     for i in range(9):
#         backup = total
#         dfs(level+1, total+num_list[i])
#         total = backup
# dfs(0, 0)
# print(cnt)

# 6번
# import copy
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
#
# used_list = [0]*N
# new_list = [0]*M
# min_result = 999
# min_list = []
# def dfs(level, result):
#     global min_result, min_list
#     if level == M:
#         if result < min_result:
#             min_list = copy.deepcopy(new_list)
#             min_result = result
#         return
#
#     for i in range(N):
#         if used_list[i] == 0:
#             used_list[i] = 1
#             new_list[level] = arr[i]
#             backup = result
#             dfs(level+1, result*arr[i])
#             used_list[i] = 0
#             result = backup
#
# a = dfs(0, 1)
# final_result = sorted(min_list)
# print(*final_result, sep = ' ')


# 7번
# dict = {'a': 15, 'b': 20, 'c': 44, 'd': 22, 'e': 55, 'f': 16, 'g': 45}
# input_arr = list(input())
# n = int(input())
# used_list = [0]*len(input_arr)
#
# max_total = 0
# def dfs(level, total):
#     global max_total
#     if level == n:
#         if total % 10 == 0:
#             if total > max_total:
#                max_total = total
#         return
#
#     for i in range(len(input_arr)):
#         if used_list[i] == 0:
#             used_list[i] = 1
#             backup = total
#             dfs(level+1, total-dict[input_arr[i]])
#             used_list[i] = 0
#             total = backup
# def init_cost(input_arr):
#     cost = 0
#     for i in range(len(input_arr)):
#         cost += dict[input_arr[i]]
#     return cost
#
# a = init_cost(input_arr)
#
# dfs(0, a)
# print(max_total)


# 8번
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# arr[0][0] = 1
# flag = 0
# def dfs(y, x):
#
#     global flag
#     if (y, x) == (n-1, n-1):
#         flag = 1
#         return
#
#     for i in range(n):
#         for j in range(n):
#             for k in range(4):
#                 if  0 <= y+dy[k] <= n-1 and 0 <= x+dx[k] <= n-1 and arr[y+dy[k]][x+dx[k]] == 0:
#                     arr[y+dy[k]][x+dx[k]] = 1
#                     dfs(y+dy[k], x+dx[k])
# dfs(0,0)
#
#
# if flag == 1:
#     print('가능')
# else:
#     print('불가능')
