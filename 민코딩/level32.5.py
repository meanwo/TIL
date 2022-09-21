# 민코딩 level 32.5 1번
# arr = [
#     ['A', 'B', 'C', 'D'],
#     ['A', 'B', 'C', 'E'],
#     ['A', 'G', 'E', 'H'],
#     ['E', 'I', 'E', 'I'],
#     ['F', 'E', 'Q', 'E'],
#     ['A', 'B', 'A', 'D']
# ]
#
# search = input()
# cnt = 0
# for i in range(len(arr)):
#     flag = 1
#     for j in range(4):
#         if search[j].isalpha() == True:
#             if arr[i][j] != search[j]:
#                 flag = 0
#                 break
#     if flag == 1:
#         cnt += 1
#
# print(cnt)

# 민코딩 level 32.5 2번
# arr = list(input())
# arr_ord = []
#
# for i in range(len(arr)):
#     arr_ord.append(ord(arr[i]))
# flag = 1
# print(*arr, sep='')
# while flag:
#     result = []
#     flag = 0
#     for i in range(len(arr_ord)):
#         arr_ord[i] -= 1
#         if arr_ord[i] >=65:
#             result.append(chr(arr_ord[i]))
#         else:
#             result.append('_')
#     for i in range(len(arr_ord)):
#         if arr_ord[i] >= 65:
#             flag = 1
#             break
#
#     print(*result, sep='')

# 민코딩 level 32.5 3번
# dx = [0, 0, 0, -1, 1]
# dy = [0, -1, 1, 0, 0]
#
# arr = [['A', 'B', 'C', 'E', 'F', 'G'], ['H', 'I', 'J', 'K', 'L', 'M'], ['N', 'O', 'P', 'Q', 'R', 'S']]
# arr_copy = [['A', 'B', 'C', 'E', 'F', 'G'], ['H', 'I', 'J', 'K', 'L', 'M'], ['N', 'O', 'P', 'Q', 'R', 'S']]
# sharp_list = [['#']* 6 for _ in range(3)]
# result = [[0]*6 for _ in range(3)]
#
# a = list(input())
#
# for i in range(len(a)):
#     for j in range(3):
#         for k in range(6):
#             if arr[j][k] == a[i]:
#                 for l in range(5):
#                     if 0 <= j+dy[l] <= 2 and 0 <= k+dx[l] <= 5:
#                         if arr[j+dy[l]][k+dx[l]] == '#':
#                             arr[j + dy[l]][k + dx[l]] = arr_copy[j + dy[l]][k + dx[l]]
#                         else:
#                             arr[j+dy[l]][k+dx[l]] = '#'
#
# for i in range(3):
#     print(*arr[i], sep = '')

# 민코딩 level 32.5 4번
# N = int(input())
# act_list = []
# for i in range(N):
#     act_list.append(list(input().split()))
#     act_list[i][0] = int(act_list[i][0])
#
# max_range = 999
# min_range = 0
# for i in range(N):
#     if act_list[i][1] == 'DOWN':
#         if act_list[i][0] < max_range:
#             max_range = act_list[i][0]
#     elif act_list[i][1] == 'UP':
#         if act_list[i][0] > min_range:
#             min_range = act_list[i][0]
#
# if (max_range - min_range) == 2:
#     print(max_range-1)
# elif (max_range - min_range) > 2:
#     print(f'%d ~ %d' %(min_range+1, max_range-1))
# else:
#     print('ERROR')

# 민코딩 level 32.5 5번
# arr = [3, 2, -1, 3, -2, 0, -1]
#
# def abc(start):
#
#     if arr[start] == 0:
#         print(f'%d번' %start)
#         return
#
#     abc(start+arr[start])
#     print(f'%d번' % start)
#
# n = int(input())
# abc(n)

# 민코딩 level 32.5 6번
# N, k = list(map(int, input().split()))
# arr = [list(map(int, input().split())) for _ in range(N)]
# for _ in range(k):
#
#     new_arr = [[0]*N for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             new_arr[i][j] = arr[N-1-j][i]
#     arr = new_arr
#
# for i in range(N):
#     print(*arr[i], sep= ' ')

# 민코딩 level 32.5 7번
# arr = [list(map(int, input().split())) for _ in range(4)]
# sum_field = 0
# for i in range(4):
#     if 0 not in arr[i]:
#         for j in range(8):
#             sum_field += arr[i][j]
# print(sum_field)


