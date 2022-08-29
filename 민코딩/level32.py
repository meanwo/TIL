# 민코딩 level 32 1번

# n = int(input())
# arr = []
# for i in range(n):
#     a, b = input().split()
#     a = int(a)
#     s = (a, b)
#     arr.append(s)
#
# result = sorted(arr, key=lambda x: (x[0], x[1]))
#
# for i in range(len(result)):
#     print(*result[i], sep=' ')

# 민코딩 level 32 2번
# N = int(input())
# medal = []
# score_list = []
# input_order = []
#
# for j in range(N):
#
#     name, score = input().split()
#     score = int(score)
#     medal.append(name)
#     input_order.append(name)
#     score_list.append(score)
#     if len(medal) > 1:
#         for k in range(j, 0, -1):
#             if score_list[k-1] < score_list[k]:
#                 medal[k-1], medal[k] = medal[k], medal[k-1]
#                 score_list[k-1], score_list[k] = score_list[k], score_list[k-1]
#             elif score_list[k-1] == score_list[k]:
#                 if input_order.index(medal[k]) > input_order.index(medal[k-1]):
#                     medal[k - 1], medal[k] = medal[k], medal[k - 1]
#                     score_list[k - 1], score_list[k] = score_list[k], score_list[k - 1]
#
#     print(*medal[0:3], sep= ' ')

# 민코딩 level 32 3번
# N = int(input())
# bomb_list = list(map(int, input().split()))
# dupli = 0
# cnt = 0
# new_list = []
# for i in range(N):
#     if bomb_list[i] == dupli:
#         cnt += 1
#     else:
#         dupli = bomb_list[i]
#         cnt = 1
#     if cnt == 3:
#         for j in range(3):
#             bomb_list[i-j] = 'b'
#             cnt = 0
# for i in range(N):
#     if bomb_list[i] != 'b':
#         new_list.append(bomb_list[i])
#
# result = sorted(new_list)
# print(*result, sep= ' ')

# 민코딩 level 32 4번
# arr = [list(map(int, input())) for _ in range(5)]
# a, b = map(int, input().split())
#
# arr[a].sort()
# arr[b].sort()
#
# for i in range(len(arr)):
#     print(arr[i][0], end= ' ')

# 민코딩 level 32 5번
# N = int(input())
# arr = []
# for i in range(N):
#     arr.append(input())
# arr.sort(key= lambda x : (len(x), x))
#
# for i in range(N):
#     print(arr[i])

# 민코딩 level 32 6번
# N, M = map(int, input().split())
# arr = []
# num_list = []
# for i in range(M):
#     num, civ = input().split()
#     num_list.append(num)
#     arr.append((num, civ))
# result = sorted(num_list, key=lambda x: (-num_list.count(x)))
#
# for i in range(M):
#     if arr[i][0] == result[0]:
#         print(arr[i][1], end = ' ')

# 민코딩 level 32 7번
# N = int(input())
# arr = [[0] * 3 for _ in range(3)]
# wind_list = []
# for i in range(N):
#     a, b, info = input().split()
#     a = int(a)
#     b = int(b)
#     arr[a][b] = int(info)
#
# wind_cnt = int(input())
# wind_list = list(map(int, input().split()))
#
# for wind in wind_list:
#     for i in range(3):
#         for j in range(3):
#             if wind >= arr[i][j]%10:
#                 if arr[i][j] < 10:
#                     arr[i][j] = 0
#                     continue
#                 arr[i][j] = int(str(arr[i][j])[0:-1])
#             elif wind < arr[i][j]%10:
#                 arr[i][j] -= wind
#
# cnt = 0
# for i in range(3):
#     for j in range(3):
#         if arr[i][j] != 0:
#             arr[i][j] = str(arr[i][j])
#             cnt += len(arr[i][j])
# print(cnt)

# 민코딩 level 32 8번
# N = int(input())
# arr = [0]*N
# for i in range(N):
#     arr[i] = input()
#
# for i in range(N):
#     if arr[i][0].isupper() == True and arr[i][1:].islower() == True:
#         continue
#     elif arr[i].islower() == True:
#         arr[i] = arr[i][0].upper()+arr[i][1:]
#     else:
#         arr[i] = arr[i].upper()
#
# arr = sorted(arr)
# for i in range(N):
#     print(arr[i])

# 민코딩 level 32 9번
# arr = list(input())[-7:-1]
# n = int(input())
# result = sorted(arr, key= lambda  x: (-arr.count(x), x))
#
# print(result[0])

# 민코딩 level 32 10번
# n = int(input())
# num_list = [list(map(int, input().split())) for _ in range(n)]
# bit_list = [list(map(int, input().split())) for _ in range(n)]
#
# result_list = []
# for i in range(n):
#     for j in range(n):
#         num_list[i][j] *= bit_list[i][j]
#         if num_list[i][j] != 0:
#             result_list.append(num_list[i][j])
#
# result = sorted(result_list, key=lambda x: (-result_list.count(x), x))
# print(*result, sep=' ')