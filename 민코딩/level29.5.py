# 민코딩 level29.5 1번
# n = int(input())
#
# arr = [3, 1, 2, 1, 3, 2, 1, 2, 1]
#
# def jump(level):
#
#     if level == n-1:
#         print('시작', end=' ')
#     if level > 8:
#         print('도착', end=' ')
#         return
#     print(arr[level], end=' ')
#     jump(level+arr[level])
#     print(arr[level], end=' ')
#     if level == n-1:
#         print('시작', end=' ')
#
# level = n-1
# result = jump(level)

# 민코딩 level29.5 2번
# n = int(input())
#
# evid = [-1, 0, 0, 1, 2, 4, 4]
# ts = [8, 3, 5, 6, 8, 9, 10]
#
# def detect(index):
#     if evid[index] == -1:
#         print(f'%d번index(출발)' %index)
#         return
#     detect(evid[index])
#     print(f'%d번index(%d시)' %(index, ts[index]))
#
# result = detect(n)

# 민코딩 level29.5 3번
# A = [list(map(int, input().split()))for _ in range(3)]
#
# for i in range(3):
#     for j in range(2):
#         if A[i][j] == A[i][j+1]:
#             print(A[i][j])
#             break
#         else:
#             print('x')
#             break

# 민코딩 level29.5 4번
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
#
# result = []
#
# a_index = 0
# b_index = 0
# while True:
#     if a_index > 3 and b_index > 3:
#         break
#
#     elif a_index > 3:
#         result.append(B[b_index])
#         b_index += 1
#
#     elif b_index > 3:
#         result.append(A[a_index])
#         a_index += 1
#
#     elif A[a_index] > B[b_index]:
#         result.append(B[b_index])
#         b_index += 1
#
#     elif A[a_index] <= B[b_index]:
#         result.append(A[a_index])
#         a_index += 1
#
# print(*result, sep=' ')

# 민코딩 level29.5 5번
# arr = [list(map(int, input().split())) for _ in range(4)]
# find_st = False
# for i in range(4):
#     for j in range(5):
#         if arr[i][j] == 1:
#             st_index = (i, j)
#             print(f'(%d,%d)' %(i, j))
#             find_st = True
#             break
#     if find_st == True:
#         break
# find_end = False
# for i in range(3, -1, -1):
#     for j in range(4, -1, -1):
#         if arr[i][j] == 1:
#             print(f'(%d,%d)' %(i, j))
#             find_end = True
#             break
#     if find_end == True:
#         break

# 민코딩 level29.5 6번
# arr = [[3, 2, 5, 3], [7, 6, 1, 6], [4, 9, 2, 7]]
# n = list(map(int, input().split()))
#
# new_arr = [[0]*4 for _ in range(3)]
# #
# for i in range(4):
#     for j in range(3):
#         new_arr[j][i] = arr[j-n[i]][i]
#
# for i in range(3):
#     print(*new_arr[i], sep ='')

# 민코딩 level29.5 7번

n = list(map(int, input().split()))
map_list = ['_', '_', '_', '_', '_']

for i in range(n[0]+1):

    if i == n[0]:
        print(['_', '_', '_', '_', '_'])
    else:
        map_list[n[0]+i] = n[1]-i
        map_list[n[0]+i-1] = '_'
        # if map_list[-1] != '_':
        #     print(['_', '_', '_', '_', '_'])
        print(map_list)
