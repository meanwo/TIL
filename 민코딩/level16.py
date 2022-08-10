# 민코딩 level 16, 1번
# a = input()
# b = input()
# c = input()
#
# answer_list = [a[-1], b[-1], c[-1]]
#
# result = ''.join(answer_list)
# print(result)

# 민코딩 level 16, 2번
# array = [['A', 'B', 'K', 'T'], ['K', 'F', 'C', 'F'], ['B', 'B', 'Q', 'Q'], ['T', 'P', 'Z', 'F']]
# str_input = input().split()
#
# cnt = 0
# for row in array:
#     for column in row:
#         if column in str_input:
#             cnt += 1
#
# print(cnt)

# 민코딩 level 16, 3번
# a = list(input())
# b = int(input())
#
# a_1 = a[0:b]
# a_2 = a[b:]
# print(*(a_1 + ['A'] + a_2), sep="")

# 민코딩 level 16, 4번
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# result = []
# for i in range(len(A)):
#     result.append(A[i]+B[3-i])
# print(*result, sep=' ')

# 민코딩 level 16, 5번
# a = list(input())
# index = int(input())
#
# a.remove(a[index])
# print(*a, sep='')

# 민코딩 level 16, 6번
# a_array = list(map(int, input().split()))
#
# for i in range(len(a_array)-1):
#     a_array[i+1] += a_array[i]
# print(*a_array)

# 민코딩 level 16, 7번
# a = [0, 0, 0]
# for i in range(3):
#     a[i] = input()
# new_a = ''.join(a)
#
# if 'M' in new_a:
#     print("M이 존재합니다")
# else:
#     print("M이 존재하지 않습니다")

#민코딩 level 16.5, 1번
# a, b, c = list(map(int, input().split()))
#
#
# for _ in range(c):
#     a_b_list = []
#     for i in range(a, b+1, 1):
#         a_b_list.append(i)
#     print(*a_b_list, sep=' ')

#민코딩 level 16.5, 2번
# k = [[0]*3 for i in range(6)]
#
# n = 65
# for j in range(2, -1, -1):
#     for i in range(5, -1, -1):
#         k[i][j] = chr(n)
#         n += 1
#
# a, b = map(int, input().split())
# print (k[a][b])

#민코딩 level 16.5, 3번
# k = [[0]*3 for i in range(2)]
# a = list(map(int, input().split()))
#
# cnt = 0
#
# max_a = a[0]
# min_a = a[0]
# max_index = [0, 0]
# min_index = [0, 0]
# for i in range(2):
#     for j in range(3):
#         k[i][j] = a[cnt]
#         cnt += 1
#         if max_a < k[i][j]:
#             max_a = k[i][j]
#             max_index = [i, j]
#         if min_a > k[i][j]:
#             min_a = k[i][j]
#             min_index = [i, j]
#
# print(f'(%d,%d)' %(max_index[0], max_index[1]))
# print(f'(%d,%d)' %(min_index[0], min_index[1]))

#민코딩 level 16.5, 4번
# a = list(map(int, input().split()))
#
# b = [0]*6
# b[0], b[1] = a[0], a[1]
#
# for i in range(4):
#     b[i+2] = b[i]*b[i+1]
#
# print(b[-1])

#민코딩 level 16.5, 5번
# a = input()
# b = input()
# c = input()
#
# print(a.replace(b, c))

#민코딩 level 16.5, 6번
# a = list(input())
# a_ord = []
#
# def maxIndex(a):
#     for i in range(len(a)):
#         a_ord.append(ord(a[i]))
#
#     max_a = max(a_ord)
#     print(a_ord.index(max_a))
#
# def minIndex(a):
#     for i in range(len(a)):
#         a_ord.append(ord(a[i]))
#
#     min_a = min(a_ord)
#     print(a_ord.index(min_a))
#
# max_i = maxIndex(a)
# min_i = minIndex(a)


#민코딩 level 16.5, 7번
# a = [[(i+1)+j*4 for i in range(4)] for j in range(7)]
#
# b = list(map(int, input().split()))
# for i in range(len(b)):
#     a[b[i]] = [0]*4
#
# for j in range(len(a)):
#     print(*a[j], sep=' ')


#민코딩 level 16.5, 8번
# n, m = input().split()
#
# a = [['A', 7, 9, 'T', 'K', 'Q'], ['M', 'I', 'N', 'C', 'O', 'D']]
#
# def isExist(n, m):
#
#     if n in a[0] or n in a[1]:
#         print('{} : 존재'.format(n))
#     else:
#         print('{} : 없음'.format(n))
#
#     if m in a[0] or m in a[1]:
#         print('{} : 존재'.format(m))
#     else:
#         print('{} : 없음'.format(m))
#
# k = isExist(n, m)

#민코딩 level 16.5, 9번
a = list(input().split())

for _ in range(2):
    for i in range(int(a[0])):
        new_a = []
        for j in range(int(a[1])):
            new_a.append(a[2])
        print(*new_a, sep='')
    print('')