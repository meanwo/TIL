# 민코딩 level 17 1번
# A = ['M', 'T', 'K', 'C']
#
# N = input()
# def isExist(N):
#     if N in A:
#         return "발견"
#     else:
#         return "미발견"
#
# b = isExist(N)
# print(b)

# 민코딩 level 17 2번
# A = [5, 9, 4, 6, 1, 5, 8, 9]
#
# n, m = map(int, input().split())
#
# if n < A.index(m):
#     print(A.index(m) - n)

# 민코딩 level 17 3번
# A = [[3, 5, 9], [4, 2, 1], [1, 1, 5]]
#
# B = [[0]*3 for _ in range(3)]
# for i in range(3):
#         B[i] = list(map(int, input().split()))
#
# sum = 0
# for i in range(3):
#     for j in range(3):
#         if A[i][j]*B[i][j] !=0:
#             sum += A[i][j]*B[i][j]
#
# print(sum)

# 민코딩 level 17 4번
# A = [['A', 'T', 'K', 'B'], ['C', 'Z', 'F', 'D'], ['H', 'G', 'E', 'I']]
#
# k, n, m = input().split()
#
# n = int(n)
# m = int(m)
#
# A_row = 0
# A_col = 0
#
# for i in range(3):
#     if k in A[i]:
#         A_row = i
#         break
#
# A_col = A[i].index(k)
# print(A[A_row+n][A_col+m])

# 민코딩 level 17 5번
# A = [[3, 5, 9], [4, 2, 1], [1, 1, 5]]
#
# x, y, z = map(int, input().split())
# A_total = []
# for i in range(3):
#     for j in range(3):
#         A_total.append(A[i][j])
#
# def isExist(x, y, z):
#     if x in A_total:
#         print('{}:존재'.format(x))
#     else:
#         print('{}:미발견'.format(x))
#
#     if y in A_total:
#         print('{}:존재'.format(y))
#     else:
#         print('{}:미발견'.format(y))
#
#     if z in A_total:
#         print('{}:존재'.format(z))
#     else:
#         print('{}:미발견'.format(z))
#
# k = isExist(x, y, z)

# 민코딩 level 17 6번
# A = [[0, 0, 0, 1], [1, 1, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
# B = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]]
# C = [[0]*4 for i in range(4)]
#
# for i in range(len(A)):
#     for j in range(len(B)):
#         # C[i][j] = A[i][j]+B[i][j]
#         if A[i][j]+B[i][j] == 0:
#             print('({},{})'.format(i, j))

# 민코딩 level 17 7번
# A = [[0, 0, 1, 0, 0], [0, 0, 1, 1, 1]]
# B = [[3, 5, 4, 1, 1], [3, 5, 2, 5, 6]]
#
# C = [[0]*5 for _ in range(2)]
#
# for i in range(2):
#     for j in range(5):
#         C[i][j] = A[i][j]*B[i][j]
#
# C_total = []
# for i in range(2):
#     for j in range(5):
#         C_total.append(C[i][j])
#
#
# n = int(input())
#
# if n in C_total:
#     print(f"%d 존재" %n)
# else:
#     print(f"%d 없음" %n)

# 민코딩 level 17 8번
# vect = ['B', 'T', 'K', "I", 'G', 'Z']
# b = list((input().split()))
#
# cnt = 0
# for spell in vect:
#     if spell in b:
#         cnt += 1
#
# print(cnt)

# # 민코딩 level 17 9번
# vect = [[3, 7, 4], [2, 2, 4], [2, 2, 5]]
#
# target = list(map(int, input().split()))
#
# target_dict = {key : 0 for key, value in dict.fromkeys(target).items()}
#
#
# for i in range(3):
#     for j in range(3):
#         if vect[i][j] == target[0]:
#             target_dict[target[0]] +=1
#         elif vect[i][j] == target[1]:
#             target_dict[target[1]] += 1
#         elif vect[i][j] == target[2]:
#             target_dict[target[2]] += 1
#
# max_key = max(target_dict, key = target_dict.get)
#
# print(max_key)

