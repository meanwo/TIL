# 민코딩 level29 1번
# n = int(input())
# arr = [list(map(int, input().split()))for _ in range(n)]
#
# path_list = []
#
# def dfs(now):
#     global path_list
#     path_list.append(now)
#
#     for i in range(n):
#         if arr[now][i] == 1:
#             dfs(i)
# result = dfs(0)
# print(*path_list, sep = ' ')

#민코딩 level29 2번
# A, B = list(map(int, input().split()))
#
# A_index = A-1
# B_index = B-1
#
# used_list = [0]*6
#
# arr = [[0, 0, 1, 0, 1, 1],
#        [1, 0, 0, 1, 0, 0],
#        [0, 0, 0, 0, 1, 0],
#        [1, 0, 0, 0, 0, 0],
#        [1, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0]]
# Min = 100
# flag = 0
# def dfs(now, cnt):
#     global Min, flag
#     if now == B_index:
#         flag = 1
#         if cnt < Min:
#             Min = cnt
#
#     for i in range(6):
#         if arr[now][i] == 1 and used_list[i] == 0:
#             used_list[i] = 1
#             dfs(i, cnt+1)
#             used_list[i] = 0

# result = dfs(A_index, 0)
# if flag == 1:
#     print(Min)
# else:
#     print(0)