# 민코딩 level 20.5 1번
# def bbq(n):
#     if n == 3:
#         return
#     bbq(n+1)
#
# result = bbq(1)

# 민코딩 level 20.5 2번
# A = list(input())
#
# for i in range(len(A)-1, -1, -1):
#     print(*A[i:], sep='')

# 민코딩 level 20.5 3번
# A = list(input())
# A_1 = []
# A_2 = []
# for i in range(len(A)):
#     if i <= (len(A)-1)//2:
#         A_1.append(A[i])
#     else:
#         A_2.append(A[i])
#
#
# if A_1 == A_2:
#     print("동일한문장")
# else:
#     print("다른문장")

# 민코딩 level 20.5 4번
# A = [list(map(int, input().split())) for _ in range(4)]
# space = input()
# B = [list(map(int, input().split())) for _ in range(4)]
# double_case = 0
# for i in range(len(A)):
#     for j in range(len(B)):
#         if A[i][j] == B[i][j] == 1:
#             double_case += 1
#
#
# if double_case != 0:
#     print("걸리다")
# else:
#     print("걸리지않는다")

# 민코딩 level 20.5 5번
# N = input()
# N_asci = ord(N)
# # print(N_asci)
# Asci_list = []
# result = []
# for i in range(-3, 4):
#     Asci_list.append(N_asci+i)
#
# for i in range(len(Asci_list)):
#     if Asci_list[i] > 90:
#         Asci_list[i] -= 26
#     elif Asci_list[i] < 65:
#         Asci_list[i] += 26
#
# for i in range(len(Asci_list)):
#     result.append(chr(Asci_list[i]))
# print(*result, sep='').

# 민코딩 level 20.5 6번
# A = list(input().split())
#
# for j in range(4, 8):
#     print(*A[:j])

# 민코딩 level 20.5 7번
# A = list(input())
#
# for i in range(len(A)):
#     print(*A[:i+1], sep ='')

# 민코딩 level 20.5 8번
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
#
# result = []
# A_index = 0
# B_index = 0
# while(1):
#
#     if A_index > 3 and B_index > 3:
#         break
#     elif A_index > 3:
#         result.append(B[B_index])
#         B_index += 1
#     elif B_index > 3:
#         result.append(A[A_index])
#         A_index += 1
#     elif A[A_index] >= B[B_index]:
#         result.append(B[B_index])
#         B_index += 1
#     elif A[A_index] < B[B_index]:
#         result.append(A[A_index])
#         A_index += 1
#
# print(*result, sep=' ')

# 민코딩 level 20.5 9번

A = [[3, 5, 4, 2, 5], [3, 3, 3, 2, 1], [3, 2, 6, 7, 8], [9, 1, 1, 3, 2]]
pat_size = list(map(int, input().split()))

max_sum = 0
max_index = 0
for i in range(4-pat_size[0]+1):
    for j in range(5-pat_size[1]+1):
        sum_arr = 0
        for k in range(pat_size[0]):
            for l in range(pat_size[1]):
                sum_arr += A[i+k][j+l]
        if max_sum < sum_arr:
            max_sum = sum_arr
            max_index = [i, j]
print(f'(%d,%d)' %(max_index[0], max_index[1]))

