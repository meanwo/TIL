# 민코딩 level 22 1번
# alphabet = ['A', 'B', 'C']
# alphabet_list = [0]*2
# def abc(level):
#     if level == 2:
#         for i in range(2):
#             print(alphabet_list[i], end = '')
#         print()
#         return
#     for j in range(3):
#         alphabet_list[level] = alphabet[j]
#         abc(level+1)
#
# result = abc(0)

# 민코딩 level 22 2번
# n = [list(input()) for _ in range(3)]
#
#
# if n[0] == n[1] == n[2]:
#     print('WOW')
# elif n[0] == n[1] or n[1] == n[2] or n[2] == n[0]:
#     print('GOOD')
# else:
#     print('BAD')

# 민코딩 level 22 3번
# n = int(input())
# arr = ['B', 'G', 'T', 'K']
# alphabet_list = [0]*n
#
# def abc(level):
#     if level == n:
#         for i in range(n):
#             print(alphabet_list[i], end='')
#         print()
#         return
#     for i in range(4):
#         alphabet_list[level] = arr[i]
#         abc(level+1)
#
# result = abc(0)

# 민코딩 level 22 4번
# n = [list(input().split()) for _ in range(5)]
#
# stair = 1
# for i in range(len(n)):
#     if n[i][0] == 'up':
#         stair += 1
#     elif n[i][0] == 'down':
#         stair -= 1
#
# if stair <= 0:
#     print(f'B%d' %(abs(stair-1)))
#
# else:
#     print(stair)

# 민코딩 level 22 5번
# n = int(input())
# clean_list = [0]*4
#
# def abc(level):
#     if level == 4:
#         for j in range(level):
#             print(clean_list[j], end ="")
#         print()
#         return
#     for i in range(1, n+1):
#         clean_list[level] = i
#         abc(level+1)
#
# result = abc(0)

# 민코딩 level 22 6번
# N = [list(input()) for _ in range(4)]
#
#
# min_len = N[0]
# max_len = N[0]
# min_index = 0
# max_index = 0
# for i in range(4):
#     if len(N[i]) > len(max_len):
#         max_len = N[i]
#         max_index = i
#     elif len(N[i]) < len(min_len):
#         min_len = N[i]
#         min_index = i
# print(f'긴문장:%d' %max_index)
# print(f'짧은문장:%d' %min_index)

# 민코딩 level 22 7번
# arr = ['A', 'B', 'C', 'D']
# alphabet_list = [0]*3
#
# input_char = list(input())
# # print(input_char)
# cnt = 0
# def abc(level):
#     global cnt
#     if level == 3:
#
#         if alphabet_list == input_char:
#             print(f'%d번째' %(cnt+1))
#         else:
#             cnt += 1
#         return
#     for i in range(4):
#         alphabet_list[level] = arr[i]
#
#         abc(level+1)
#
# result = abc(0)

# 민코딩 level 22 8번
# three_array = [[[2, 4], [1, 5]], [[2, 3], [3, 6]], [[7, 3], [1, 5]]]
#
# n = int(input())
# two_array = three_array[n]
# two_array_list = []
# for i in range(2):
#     for j in range(2):
#          two_array_list.append(two_array[i][j])
#
#
# print(f'MAX=%d'% max(two_array_list))
# print(f'MIN=%d'% min(two_array_list))


# 민코딩 level 22 9번
password_list = ['Jason', 'Dr.tom', 'EXEXI', 'GK12P', 'POW']

n = input()

if n in password_list:
    print('암호해제')
else:
    print('암호틀림')
