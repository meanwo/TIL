# 민코딩 level 17.5 1번
# A = [3, 4, 1, 1, 2, 6, 8, 7, 8, 9, 10]
# n = int(input())
#
# def getSum(n):
#     sum_A = 0
#     for i in range(5):
#         sum_A += A[n+i]
#     print(sum_A)
#
# new = getSum(n)

# 민코딩 level 17.5 2번
# A = [3, 7, 4, 1, 2, 6]
# univer = [[0]*2 for i in range(2)]
#
# for i in range(2):
#     univer[i][:] = map(int, (input().split()))
#
# def isExist(univer):
#     for i in range(2):
#         for j in range(2):
#             if univer[i][j] in A:
#                 univer[i][j] = 'OK'
#             else:
#                 univer[i][j] = 'NO'
#
#     for i in range(2):
#         print(*univer[i][:], sep=' ')
#
# answer = isExist(univer)

# 민코딩 level 17.5 3번
# a_list = [[0] for i in range(2)]
# for i in range(2):
#     a_list[i] = input()
#
# def isSame(a_list):
#     if a_list[0] == a_list[1]:
#         return 1
#     return 0
#
# answer = isSame(a_list)
#
# if answer == 1:
#     print("동명")
# else:
#     print("남남")

# 민코딩 level 17.5 4번
# A =[['G', 'K', 'T'], ['P', 'A', 'C']]
# n = list(input().split())
#
# def isExist(n):
#     cnt = 0
#     A_list = []
#     for i in range(2):
#         for j in range(3):
#             A_list.append(A[i][j])
#
#     if n[0] in A_list:
#        cnt += 1
#     if n[1] in A_list:
#         cnt +=1
#
#     return cnt
#
# k = isExist(n)
#
# if k == 2:
#     print("대발견")
# elif k == 1:
#     print("중발견")
# elif k == 0:
#     print("미발견")

# 민코딩 level 17.5 5번
# vect = [3, 5, 4, 2, 6, 6, 5]
# bit = list(map(int, input().split()))
# new_list = []
# for i in range(len(vect)):
#     new_list.append(vect[i]*bit[i])
#     if new_list[i] != 0:
#         new_list[i] = 7
#
# print(*new_list, sep='')

# 민코딩 level 17.5 6번
# pwd_input = list(map(int, input().split()))
# pwd = [3, 7, 4, 9]
# def isSame(pwd_input):
#     if pwd == pwd_input:
#         return 'pass'
#     return 'fail'
#
# answer = isSame(pwd_input)
# print(answer)

# 민코딩 level 17.5 7번
# info = [[10, 20], [30, 60], [100, 150], [200, 300]]
# cnt_list = [0]*4
# input_fruit = list(map(int, input().split()))
#
# for i in range(len(input_fruit)):
#     for j in range(len(info)):
#         if input_fruit[i] >= info[j][0] and input_fruit[i] <= info[j][1]:
#             cnt_list[j] += 1
#
#
# for i in range(len(info)):
#     print('lev{}:{}'.format(i, cnt_list[i]))

# 민코딩 level 17.5 8번
# map_array = [[3, 55, 42], [-5, -9, -10]]
# pix_array = [list(map(int, input().split())) for _ in range(2)]
# map_array_list = []
# for i in range(2):
#     for j in range(3):
#         map_array_list.append(map_array[i][j])
#
# for i in range(2):
#     for j in range(2):
#         # pix_array_list.append(pix_array[i][j])
#         if pix_array[i][j] in map_array_list:
#             pix_array[i][j] = 'Y'
#         else:
#             pix_array[i][j] = 'N'
#
# for i in range(2):
#     print(*pix_array[i])

# 민코딩 level 17.5 9번
#
# arr = list(map(int, input().split()))
# masking = [1, 0, 1, 0, 1, 0]
#
# new_list = []
# masking_array = []
# for i in range(len(arr)):
#     new_list.append(arr[i]*masking[i])
#
# for i in range(len(new_list)):
#     if new_list[i] > 0:
#         masking_array.append(new_list[i])
#
# min_factor = min(masking_array)
#
# print('arr[{}]={}'.format(new_list.index(min_factor), min_factor))

# 민코딩 level 17.5 10번
# masking = [list(map(int, input().split())) for _ in range(3)]
# A = [[3, 1, 9], [7, 2, 1], [1, 0, 8]]
#
# A_list = []
# for i in range(3):
#     for j in range(3):
#         A[i][j] *= masking[i][j]
#         A_list.append(A[i][j])
#
# if (3 or 4 or 5) in A_list:
#     print("발견")
# else:
#     print("미발견")

# 민코딩 level 17.5 11번
# A = [3, 5, 4, 2]
# n = list(map(int, input().split()))
# sum_A = 0
# for i in range(len(A)):
#     sum_A += A[i]*n[i]
#
# print(sum_A)

# 민코딩 level 17.5 12번
# A = [[0]*5 for _ in range(5)]
# n = input()
#
# input_index = []
# asci_number = 65
# for i in range(5):
#     for j in range(5):
#         A[i][j] = chr(asci_number)
#         asci_number += 1
#         if A[i][j] == n:
#             input_index.append(i)
#             input_index.append(j)
#
# print('{},{}'.format(input_index[0]-2, input_index[1]-2))


