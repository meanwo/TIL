# 민코딩 21 1번
# def call(n):
#     if n == 3:
#         return
#     for i in range(3):
#         call(n+1)
#
# result = call(0)

# 민코딩 21 2번
# admin_id = "qlqlaqkq"
# admin_pwd = "tkaruqtkf"
#
# ID = input()
# PASSWORD = input()
#
# if ID == admin_id and PASSWORD == admin_pwd:
#     print("LOGIN")
# else:
#     print("INVALID")

# 민코딩 21 3번
# def call(level, branch):
#
#     if level == 0:
#         return
#     for i in range(branch):
#         call(level-1, branch)
#
# result = call(2, 3)

# 민코딩 21 4번
# level = int(input())
# constant = level
# def call(level):
#     print(abs(constant-level), end="")
#     if level == 0:
#         return
#     for i in range(2):
#         call(level-1)
#
# result = call(level)

# 민코딩 21 5번
# A = [list(input()) for _ in range(3)]
# len_index = 0
# for i in range(3):
#     if len(A[i][:]) > len(A[len_index][:]):
#         len_index = i
# # print(len_a)
# A[0], A[len_index] = A[len_index], A[0]
#
# for i in range(3):
#     print(*A[i], sep='')

# 민코딩 21 6번
# cnt = 0
# n, m = map(int, input().split())
# def call(branch, level):
#     global cnt
#     cnt += 1
#     if level == 0:
#         return
#     for i in range(branch):
#         call(branch, level-1)
#
# result = call(n, m)
# print(cnt)

# 민코딩 21 7번
# A = input()
# len_A = len(A)
#
# def call(len_A):
#     print(len_A, end=' ')
#     if len_A == 1:
#         return
#     call(len_A-1)
#     print(len_A, end= ' ')
#
# result = call(len_A)

# 민코딩 21 8번
# n = int(input())
# command = list(input() for _ in range(n))
# current = [5, 5]
# #
# for i in range(n):
#     if command[i] == 'up':
#         current[0] -= 1
#     elif command[i] == 'down':
#         current[0] += 1
#     elif command[i] == 'left':
#         current[1] -= 1
#     elif command[i] == 'right':
#         current[1] += 1
#     elif command[i] == 'click':
#         print(f'%d,%d' %(current[0],current[1]))


