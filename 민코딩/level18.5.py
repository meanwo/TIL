# # 민코딩 level 18.5 1번
# A = ['G', 'K', 'G']
# n = input().split()
# A_asci = []
# cnt_list = [0]*100
#
# cnt_above_3 = 0
#
# for i in range(3):
#     A.append(n[i])
#
#
# for i in range(len(A)):
#     A_asci.append(ord(A[i]))
#     cnt_list[A_asci[i]] += 1
#
# for i in range(len(cnt_list)):
#     if cnt_list[i] >= 3:
#         cnt_above_3 += 1
#
# if cnt_above_3 == 0:
#     print('없음')
# else:
#     print('있음')

# 민코딩 level 18.5 2번
# A = list(map(int, input().split()))
# cnt_list =[0]*7
# flag = 0
# for i in range(len(A)):
#     cnt_list[A[i]] += 1
#
# for i in range(len(cnt_list)):
#     if cnt_list[i] > 1:
#         flag = 1
#
#
# if flag == 1:
#     print("도플갱어 발견")
# else:
#     print("미발견")

# 민코딩 level 18.5 3번
# A = list(input())
# A_asci= []
# cnt_list = [0]*100
# max_factor = 0
# for i in range(len(A)):
#     A_asci.append(ord(A[i]))
#
# for i in range(len(A_asci)):
#     cnt_list[A_asci[i]] += 1
#
# for i in range(len(cnt_list)):
#    if cnt_list[i] > max_factor:
#        max_factor = cnt_list[i]
#        max_index = i
#
# print(chr(max_index))

# 민코딩 level 18.5 4번
# up = list(map(int, input().split()))
# down = list(map(int, input().split()))
# cnt = 0
# for i in range(len(up)):
#     if up[i] and down[i] == 1:
#        cnt += 1
#
# print(f'%d개'%cnt)

# 민코딩 level 18.5 5번
# A = ['A', 'T', 'K', 'P', 'T', 'C', 'A', 'B', 'C']
#
# n, m = input().split()
#
# cnt_left = 0
# cnt_right = 0
#
# for i in range(len(A)):
#     if A[i] == n:
#         cnt_left = i
#         break
#
# for i in range(len(A)-1, -1, -1):
#     if A[i] == m:
#         cnt_right = i
#         break
#
#
# print(cnt_right-cnt_left)

# 민코딩 level 18.5 6번
# A = [[3, 5, 1], [4, 2, 6]]
# A_list =[]
# people = list(map(int, input().split()))
#
# for i in range(2):
#     for j in range(3):
#         A_list.append(A[i][j])
#
# for i in range(len(people)):
#     if people[i] in A_list:
#         print(f'%d번 합격' %people[i])
#     else:
#         print(f'%d번 불합격' %people[i])

# 민코딩 level 18.5 7번
# vect = 'MINCODING'
# vect_asci = []
# cnt_list = [0]*100
# OX_list = []
# for i in range(len(vect)):
#     vect_asci.append(ord(vect[i]))
#
# n = int(input())
# A = list(input().split())
# A_asci = []
#
# for i in range(len(A)):
#     A_asci.append(ord(A[i]))
#
# for i in range(len(vect)):
#     cnt_list[vect_asci[i]] += 1
#
# for i in range(len(A_asci)):
#     if cnt_list[A_asci[i]] != 0:
#         OX_list.append('O')
#     else:
#         OX_list.append('X')
#
# print(*OX_list, sep='')

# 민코딩 level 18.5 8번
# list_A = []
# A_asci = []
# cnt_list = [0]*100
# flag = 0
# for i in range(3):
#     list_A.append(list(input()))
#
# for i in range(3):
#     for j in range(len(list_A[i])):
#         A_asci.append(ord(list_A[i][j]))
#
# for i in range(len(A_asci)):
#     cnt_list[A_asci[i]] += 1
#
# for i in range(len(cnt_list)):
#     if cnt_list[i] > 1:
#         flag = 1
#
# if flag == 1:
#     print('No')
# else:
#     print('Perfect')

# 민코딩 level 18.5 9번
A = list(input())
A_asci = []
cnt_list = [0]*100
result_list = []
for i in range(len(A)):
    A_asci.append(ord(A[i]))

print(A_asci)

for i in range(len(A_asci)):
    cnt_list[A_asci[i]] += 1

for i in range(len(cnt_list)):
    if cnt_list[i] > 1:
        cnt_list[i] = 1

print(cnt_list)
# for i in range(len(A_asci)):
#     result_list.append(A_asci[i])
#     cnt_list[i] -= 1
# print(result_list)

