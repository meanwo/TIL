# 민코딩 level28 1번
# name = ['Amy', 'Bob', 'Chloe', 'Diane', 'Edger']
#
# arr = [[0, 0, 0, 0, 1],
#        [1, 0, 0, 0, 0],
#        [0, 1, 0, 0, 0],
#        [0, 1, 0, 0, 0],
#        [0, 0, 0, 0, 0]]
#
# cnt = [0]*5
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         cnt[i] += arr[j][i]
#
# max_index = 0
# for i in range(len(cnt)):
#     if cnt[max_index] < cnt[i]:
#         max_index = i
# print(name[max_index])

# 민코딩 level28 2번
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# # print(arr)
#
# boss_list =[]
# under_list = []
# for i in range(n):
#     if arr[i][0] == 1:
#         boss_list.append(i)
# print('boss:', end ='')
#
# for i in range(len(boss_list)):
#     print(boss_list[i], end = ' ')
#     print()
#
# for i in range(n):
#     if arr[0][i] == 1:
#         under_list.append(i)
# print('under:', end ='')
#
# for i in range(len(under_list)):
#     print(under_list[i], end = ' ')


# 민코딩 level28 3번
arr = [[0, 1, 1, 0, 0, 0, 0, 1],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 1, 0, 1, 0],
       [0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0]]

name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

n = input()
now = name.index(n)
parents_index = 999
bro_index = []
flag = 0

def dfs(now):
    for i in range(len(arr)):
        if arr[i][now] == 1:
            parents_index = i

    for i in range(len(arr[0])):
        if arr[parents_index][i] == 1:
            bro_index.append(i)

if now == 0 or 5:
    print('없음')
else:
    result = dfs(now)
# print(result)
    bro_index.remove(now)

for i in range(len(bro_index)):
    print(name[bro_index[i]], end= ' ')

# 민코딩 level28 4번
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# path_list = []
# def dfs(now):
#     global path_list
#     path_list.append(now)
#     for i in range(n):
#         if arr[now][i] == 1:
#             dfs(i)
# result = dfs(0)
# print(*path_list, sep = ' ')


# 민코딩 level28 5번
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# path_list = [0]*3
# def dfs(level, now):
#     # global path_list
#     # path_list.append(now)
#     if level == 2:
#         for i in range(len(path_list)):
#             print(path_list[i], end = ' ')
#         print()
#         return
#
#     for i in range(n):
#         if arr[now][i] == 1:
#             path_list[level+1] = i
#             dfs(level+1, i)
# result = dfs(0, 0)

# 민코딩 level28 6번
# name = list(input())
# arr = [list(map(int, input().split())) for _ in range(8)]
# path_list = []
#
# def dfs(now):
#     global path_list
#     path_list.append(now)
#
#     for i in range(8):
#         if arr[now][i] == 1:
#             dfs(i)
#
# result = dfs(0)
#
# for i in range(len(path_list)):
#     print(*name[path_list[i]], end='')