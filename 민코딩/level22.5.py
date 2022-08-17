# 민코딩 level 22.5 1번
# A = [[['A', 'T', 'B'], ['C', 'C', 'B']], [['A', 'A', 'A'], ['B', 'B', 'C']]]
#
# n = input()
#
# A_list = []
# for i in range(2):
#     for j in range(2):
#         for k in range(3):
#             A_list.append(A[i][j][k])
#
# if n in A_list:
#     print("발견")
# else:
#     print("미발견")

# 민코딩 level 22.5 2번
# n = int(input())
# date_list = [0]*n
# xo_list = ['x', 'o']
# def abc(level):
#     if level == n:
#         for i in range(level):
#             print(date_list[i], end='')
#         print()
#         return
#     for i in range(len(xo_list)):
#         date_list[level] = xo_list[i]
#         abc(level+1)
#
# result = abc(0)

# 민코딩 level 22.5 3번
# A = [[[0]*3 for _ in range(3)] for _ in range(3)]
#
# n = input()
# n_asci = ord(n)
#
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             A[i][j][k] = chr(n_asci+i)
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             print(*A[i][j][k], end='')
#         print()
#     print()

# 민코딩 level 22.5 4번
# A = [[[0]*3 for _ in range(2)]for _ in range(3)]
#
# # ab = list(map(int, input().split()))
# a, b = map(int, input().split())
# for i in range(3):
#     for j in range(2):
#         for k in range(3):
#             if j ==0 :
#                 A[i][j][k] = a
#             else:
#                 A[i][j][k] = b
#
# for i in range(3):
#     for j in range(2):
#         for k in range(3):
#             print(A[i][j][k], end=' ')
#         print()
#     print()

# 민코딩 level 22.5 5번
# map_array = [[3, 5, 4, 2, 2, 3], [1, 3, 3, 3, 4, 2], [5, 4, 4, 2, 3, 5]]
# price_array = ["T", 'P', 'G', 'K', 'C']
#
# input_code = list(input().split())
#
# input_code[0] = ord(input_code[0])
# input_code[1] = int(input_code[1])
# # print(input_code)
#
# price_index = map_array[input_code[0]-65][input_code[1]-1]
# print(price_array[price_index-1])

# 민코딩 level 22.5 6번
# N = [list(input().split()) for _ in range(4)]
#
# for i in range(1, 4):
#     for j in range(4-i):
#         if len(N[j][0]) > len(N[j+1][0]):
#             N[j][0], N[j+1][0] = N[j+1][0], N[j][0]
#
#
# for i in range(4):
#     for j in range(1):
#         print(*N[i][j], sep='')

# 민코딩 level 22.5 7번
n = int(input())
ABCD = [
    [[' ', '#', ' '],
     ['#', ' ', '#'],
     ['#', '#', '#'],
     ['#', ' ', '#'],
     ['#', ' ', '#']],
    [['#', '#', '#'],
     ['#', ' ', '#'],
     ['#', '#', '#'],
     ['#', ' ', '#'],
     ['#', '#', '#']],
    [['#', '#', '#'],
     ['#', ' ', '#'],
     ['#', ' ', ' '],
     ['#', ' ', '#'],
     ['#', '#', '#']],
    [['#', '#', ' '],
     ['#', ' ', '#'],
     ['#', ' ', '#'],
     ['#', ' ', '#'],
     ['#', '#', ' ']]
    ]

for j in range(5):
    for k in range(3):
        print(ABCD[n][j][k], end= '')
    print()