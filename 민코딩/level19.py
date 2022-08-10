# 민코딩 level 19 1번
# arr = [[3, 5, 4], [1, 1, 2], [1, 3, 9]]
# sum_arr = 0
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
# a, b = map(int, input().split())
#
# for i in range(4):
#         if a+dx[i] >= 0 and a+dx[i] <=2 and b+dy[i] >=0 and b+dy[i] <=2:
#             sum_arr += arr[a+dx[i]][b+dy[i]]
# print(sum_arr)

# 민코딩 level 19 2번
# map_array = [[3, 3, 5, 3, 1], [2, 2, 4, 2, 6], [4, 9, 2, 3, 4], [1, 1, 1, 1, 1], [3, 3, 5, 9, 2]]
#
# sum_arr = 0
#
# def sum():
#     sum_arr = 0
#     max_sum = 0
#     dx = [1, 1, -1, -1]
#     dy = [1, -1, 1, -1]
#     for i in range(5):
#         for j in range(5):
#             sum_arr = 0
#             for k in range(4):
#                 if i+dx[k] >= 0 and i+dx[k] <= 4 and j+dy[k] >=0 and j+dy[k] <=4:
#                     sum_arr += map_array[i+dx[k]][j+dy[k]]
#
#             if max_sum < sum_arr:
#                 max_sum = sum_arr
#                 max_index = [i, j]
#     return max_index
#
# result = sum()
# print(*result)

# 민코딩 level 19 3번
# A = [['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_']]
#
# bomb = [list(map(int, input().split())) for _ in range(2)]
#
# dx = [-1, 0, 1, 1, 1, 0, -1, -1]
# dy = [1, 1, 1, 0, -1, -1, -1, 0]
#
# for i in range(2):
#     for j in range(8):
#         if bomb[i][0]+dx[j] >= 0 and bomb[i][0]+dx[j] <= 3 and bomb[i][1]+dy[j] >=0 and bomb[i][1]+dy[j] <= 4:
#             A[bomb[i][0]+dx[j]][bomb[i][1]+dy[j]] = '#'
#
# for i in range(4):
#     print(*A[i])

# 민코딩 level 19 7번
# point = [list(map(int, input().split())) for _ in range(4)]
# vect = [[0]*3 for _ in range(4)]
#
#
# for i in range(4):
#     vect[point[i][0]][point[i][1]] = 5
#
# for i in range(4):
#     print(*vect[i], sep=' ')

# 민코딩 level 19 8번
# A = [list(map(int, input().split())) for _ in range(4)]
#
# def rectSum():
#     max_rect = 0
#     for n in range(3):
#         for m in range(2):
#             sum_rect = 0
#             for i in range(2):
#                 for j in range(3):
#                     sum_rect += A[i+n][j+m]
#             if max_rect < sum_rect:
#                 max_rect = sum_rect
#                 max_index = n, m
#     return max_index
#
# result = rectSum()
# print(f'(%d,%d)' %(result[0], result[1]))