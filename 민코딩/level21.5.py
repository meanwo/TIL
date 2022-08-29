# 민코딩 21.5 1번

# A = [list(input()) for _ in range(4)]
#
# for i in range(4):
#     for j in range(3):
#         if A[i][j] == 'A':
#             A_index = [i, j]
#         elif A[i][j] == 'B':
#             B_index = [i, j]
#
# print(abs(A_index[0]-B_index[0]) + abs(A_index[1]-B_index[1]))

# 민코딩 21.5 2번

# A = [[3, 4, 1, 5], [3, 4, 1, 3], [5, 2, 3, 6]]
# sum = [0]*4
# for i in range(4):
#     for j in range(3):
#         sum[i] += (A[j][i])
# index = int(input())
# print(sum[index])

# 민코딩 21.5 3번
# A = list(input())
# select_chr = list(input().split())
# change_index = [0]*2
# for i in range(2):
#     if select_chr[i] in A:
#         change_index[i] = A.index(select_chr[i])
#
# for i in range(2):
#     if change_index[i] == 0:
#         A[change_index[i]+1] = '#'
#     elif change_index[i] == len(A)-1:
#         A[change_index[i]-1] = '#'
#     else:
#         A[change_index[i]-1] = '#'
#         A[change_index[i]+1] = '#'
# #
# print(*A, sep ='')

#수정 필요 코드
# sen = list(input())
# t1,t2= input().split()
#
# for i in range(len(sen)): #5일때 0,1,2,3,4
#     if t1 == sen[i] or t2 == sen[i]:
#         if i-1<0 or i+1>4:
#             print(i)
#             continue
#         print(i)
#         sen[i-1] = '#'
#         sen[i+1] = '#'
#
# print(sen)


# 민코딩 21.5 4번
# A = [list(input()) for _ in range(4)]
#
# for i in range(3):
#     for j in range(3, 0, -1):
#         for k in range(j):
#             if A[k][i] != '_' and A[k+1][i] == '_':
#                 A[k][i], A[k+1][i] = A[k+1][i], A[k][i]
#
# for i in range(4):
#     print(*A[i], sep='')

# 민코딩 21.5 5번
# vect = list(map(int, input().split()))
# bucket = [0]*10
# new_list = [0]*8
# for i in range(len(vect)):
#     bucket[vect[i]] += 1
#
# for i in range(1, len(bucket)):
#     bucket[i] += bucket[i-1]
#
# for i in range(len(vect)):
#     new_list[bucket[vect[i]]-1] = vect[i]
#     bucket[vect[i]] -= 1
#
# print(*new_list, sep=' ')

# 민코딩 21.5 6번
# A = [[1, 5, 3], [4, 5, 5], [3, 3, 5], [4, 6, 2]]
#
# a, b = list(map(int, input().split()))
#
# for i in range(4):
#     for j in range(3):
#         if A[i][j]>=a and A[i][j]<=b:
#             A[i][j] = '#'
#
# for i in range(4):
#     print(*A[i], sep = ' ')

# 민코딩 21.5 7번
# 없음: 0, 백돌: 1, 흑돌: 2
# A = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0], [0, 1, 2, 0, 2, 1, 0], [0, 0, 1, 2, 1, 0, 0], [0, 0, 2, 1, 0, 1, 0], [0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
#
# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]
#
# my_position = list(map(int, input().split()))
#
# cnt = 0
# for i in range(4):
#     if A[my_position[0]+dy[i]][my_position[1]+dx[i]] == 2:
#         white_space = 0
#         empty_space = 0
#
#         for j in range(4):
#             if A[my_position[0]+dy[i]+dy[j]][my_position[1]+dx[i]+dx[j]] == 1:
#                 white_space += 1
#             elif A[my_position[0]+dy[i]+dy[j]][my_position[1]+dx[i]+dx[j]] == 0:
#                 empty_space += 1
#
#         if white_space == 3 and empty_space == 1:
#             cnt += 1
#
# print(cnt)

# # 민코딩 21.5 8번
# A = [['_', '_', '_'], ['_', '_', '_'], ['A', 'T', 'K'], ['_', '_', '_'], ['_', '_', '_']]
# command = [list(input().split()) for _ in range(7)]
#
# model_name = []
# model_index = []
# model_dict = {}
# # 초기 위치
# for i in range(5):
#     for j in range(3):
#         if A[i][j] != '_':
#             model_dict[A[i][j]] = [i, j]
#
# for i in range(7):
#     # print(model_dict[command[i][0]][0], model_dict[command[i][0]][1])
#     if command[i][1] == 'UP':
#         model_dict[command[i][0]][0] -= 1
#     elif command[i][1] == 'DOWN':
#         model_dict[command[i][0]][0] += 1
#     elif command[i][1] == 'LEFT':
#         model_dict[command[i][0]][1] -= 1
#     elif command[i][1] == 'RIGHT':
#         model_dict[command[i][0]][1] += 1
#
# new_A = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
#
# # 최종 위치
# for key, value in model_dict.items():
#     new_A[value[0]][value[1]] = key
#
# for i in range(5):
#     print(*new_A[i], sep='')

# # 민코딩 21.5 8번(함수)
# arr = [list(input().split()) for _ in range(7)] # 행마다 [model, cmd]
#
# loc = [
# ['_', '_', '_'],
# ['_', '_', '_'],
# ['A', 'T', 'K'],
# ['_', '_', '_'],
# ['_', '_', '_']
# ]
#
# # 모델 위치 찾기
# def Model(model):
#     for i in range(5):
#         for j in range(3):
#             if loc[i][j] == model:
#                 return i, j   # (i, j) 리턴 됨
#
# # 명령어 받기
# for y in range(7):
#     i, j = Model(arr[y][0])
#     if arr[y][1] == 'UP':
#         loc[i][j], loc[i-1][j] = loc[i-1][j], loc[i][j]
#     if arr[y][1] == 'DOWN':
#         loc[i][j], loc[i+1][j] = loc[i+1][j], loc[i][j]
#     if arr[y][1] == 'LEFT':
#         loc[i][j], loc[i][j-1] = loc[i][j-1], loc[i][j]
#     if arr[y][1] == 'RIGHT':
#         loc[i][j], loc[i+1][j] = loc[i+1][j], loc[i][j]
#
# for i in range(5):
#     print(*loc[i], sep='')