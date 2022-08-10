# 이진탐색
# n = int(input())
# arr = list(map(int, input().split()))
# target = int(input())
#
#
# def binary_search(st, ed, value):
#     while (1):
#         mid = (st+ed)//2
#         if arr[mid] == value:
#             return 1
#         elif arr[mid] > value:
#             ed = mid-1
#         elif arr[mid] < value:
#             st = mid+1
#
#         if st > ed:
#             return 0
#
# arr.sort()
# ret = binary_search(0, n-1, target)
#
# if ret:
#     print("찾음")
# else:
#     print("없음")

# parametric search ex1
# n = 10
# max_a = 0
# battery = "*_________"
#
# def parametric(st, ed):
#     max_a = -1
#     while 1:
#         mid = (st+ed)//2
#         if battery[mid] == '*':
#             st = mid+1
#             max_a = mid
#         elif battery[mid] == '_':
#             ed = mid-1
#
#         if st > ed:
#
#             return max_a
#
# ret = parametric(0, n-1)
# print(ret+1)

# parametric search ex2
# curser = [
#     '##########',
#     '##########',
#     '###_______',
#     '__________',
#     '__________',
#     '__________',
# ]
# curser_list = []
# def find_curser(st, en, st_2, en_2):
#
#     while(1):
#         mid = (st+en)//2
#         if curser[mid][0] == '#':
#             st = mid+1
#             curser_array = mid
#         else:
#             en = mid-1
#         if st > en:
#             break
#
#     while(1):
#         mid_col = (st_2+en_2)//2
#         if curser[curser_array][mid_col] == '#':
#             st_2 = mid_col + 1
#             curser_col = mid_col
#         else:
#             en_2= mid_col - 1
#         if st_2 > en_2:
#             break
#
#
#     return curser_array+1, curser_col+1
#
# result = find_curser(0, 5, 0, 9)
# print(result)

# 1
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
A_transpose = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        A_transpose[i][j] = A[j][i]

print(A_transpose)

#2
A_reverse = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        A_reverse[i][j] = A[2-j][2-i]
print(A_reverse)

#3
A_zigzag = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i%2 == 1:
            A_zigzag[i][j] = A[i][2-j]
        else:
            A_zigzag[i][j] = A[i][j]
print(A_zigzag)

# 4
A_low = 0
A_upper = 0
for i in range(N):
    for j in range(N):
        if i > j:
            A_low += A[i][j]
        elif i < j:
            A_upper += A[i][j]

print(A_low, A_upper)

#5

A_diagonal= [0]*(2*(len(A)-1)+1)
for i in range(N):
    for j in range(N):
        A_diagonal[i+j] += A[i][j]
print(A_diagonal)