# 민코딩 level 19.5 2번
# A = [list(map(int, input().split())) for _ in range(5)]
#
# dx = [-1, 0, 1, 1, 1, 0, -1, -1]
# dy = [1, 1, 1, 0, -1, -1, -1, 0]
# sum_around = 0
# flag = 0
# for i in range(5):
#     for j in range(4):
#         for k in range(8):
#             if A[i][j] == 1:
#                 if dx[k]+j >=0 and dx[k]+j <=3 and dy[k]+i >= 0 and dy[k]+i <= 4:
#                     sum_around += A[dy[k]+i][dx[k]+j]
#
#         if sum_around > 0:
#             flag = 0
#             break
#         else:
#             flag = 1
#
# if flag == 1:
#     print("안정된 상태")
# elif flag == 0:
#     print("불안정한 상태")

# 민코딩 level 19.5 3번
# A = list(map(int, input().split()))
# new_array = [[0] * 4 for _ in range(4)]
# four_array = [[0] * 4 for _ in range(4)]
# n = 1
# m = 1
# for i in range(4):
#     for j in range(4):
#         four_array[i][j] = n
#         if four_array[i][j] in A:
#             new_array[i][j] = m
#             m += 1
#         n += 1
#
# for i in range(4):
#     print(*new_array[i])

# 민코딩 level 19.5 4번
# A = [[0]*4 for _ in range(4)]
# # print(A[:][0])
# n = []
# for i in range(3):
#     n.append(list(input().split()))
#
# for i in range(3):
#     for j in range(4):
#         if n[i][0] == 'G':
#             A[int(n[i][1])][j] = 1
#
#         elif n[i][0] == 'S':
#             A[j][int(n[i][1])] = 1
#
# for i in range(4):
#     print(*A[i], sep=' ')

# 민코딩 level 19.5 6번
# A = [['A', 'B', 'G', 'K'], ['T', 'T', 'A', 'B'], ['A', 'C', 'C', 'D']]
#
# dx = [0, 1, 0, 1]
# dy = [0, 0, 1, 1]
# match_count = 0
#
# pattern = [list(input()) for _ in range(2)]
#
# for i in range(2):
#     for j in range(3):
#         cnt = 0
#         for k in range(4):
#             if A[i+dy[k]][j+dx[k]] == pattern[dy[k]][dx[k]]:
#                 cnt += 1
#                 if cnt == 4:
#                     match_count += 1
#
# if match_count > 0:
#     print(f'발견(%d개)' %match_count)
# else:
#     print("미발견")

# 민코딩 level 19.5 7번
# map_array = [[3, 5, 1], [3, 8, 1], [1, 1, 5]]
#
# dx = [0, 1, 0, 1]
# dy = [0, 0, 1, 1]
# bit_array = [list(map(int, input().split())) for _ in range(2)]
#
# max_sum = 0
# for i in range(2):
#     for j in range(2):
#         sum_array = 0
#         for k in range(4):
#             sum_array += map_array[i+dy[k]][j+dx[k]]*bit_array[dx[k]][dy[k]]
#         if sum_array > max_sum:
#             max_sum = sum_array
#             max_index = (i, j)
# print(f'(%d,%d)' %(max_index[0], max_index[1]))





