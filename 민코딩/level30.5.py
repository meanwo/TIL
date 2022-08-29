# 민코딩 level 30.5 1번
# clock_arr = [[12, 9], [3, 6]]
# clock_list = []
# new_clock = []
# for i in range(2):
#     for j in range(2):
#         clock_list.append(clock_arr[i][j])
#
#
# n = int(input())
# m = (n/90)%4
# def rot(m, clock_list):
#     if m == 0:
#         return clock_list
#     clock_list = [clock_list[1], clock_list[3], clock_list[0], clock_list[2]]
#     return rot(m-1, clock_list)
#
# result = rot(m, clock_list)
# print(*result, sep= ' ')

# 민코딩 level 30.5 2번

# kick = ['o', 'x']
# n = int(input())
# result_list = [0]*n
#
# def call(level):
#     if level == n:
#         for i in range(n):
#             print(result_list[i], end='')
#         print()
#         return
#
#     for i in range(2):
#         result_list[level] = kick[i]
#         call(level+1)
# result = call(0)

# 민코딩 level 30.5 3번
# n = int(input())
# arr = [1, 5, 4, 2, -5, -7]
# for i in range(5):
#     for j in range(5-i):
#         if arr[i] < arr[i+j+1]:
#             arr[i], arr[i+j+1] = arr[i+j+1], arr[i]
#
# print(arr[n-1])

# 민코딩 level 30.5 4번
# num_list = [list(input()) for _ in range(3)]
# num_list2 = []
# max_len = len(num_list[0])
# for i in range(len(num_list)):
#     if max_len <= len(num_list[i]):
#         max_len = len(num_list[i])
#
# for i in range(len(num_list)):
#     if max_len == len(num_list[i]):
#         num_list2.append(num_list[i])
#
# a = 0
# while True:
#     if num_list2[0][a] == '1' and num_list2[1][a] == '1':
#         a += 1
#     elif num_list2[0][a] == '0':
#         print(*num_list2[1], sep='')
#         break
#     elif num_list2[1][a] == '0':
#         print(*num_list2[0], sep='')
#         break

# 민코딩 level 30.5 5번
# arr = list(input())
# n = int(input())
#
# selected = [0]*n
#
# def abc(level):
#     if level == n:
#         for i in range(n):
#             print(selected[i], end ='')
#         print()
#         return
#     for i in range(len(arr)):
#         selected[level] = arr[i]
#         abc(level+1)
#
# result = abc(0)

# 민코딩 level 30.5 6번
# selected = [0]*4
# cnt = 0
# arr = []
# for i in range(65, 91):
#     arr.append(chr(i))
#
# def abc(level):
#     global cnt
#     if level == 4:
#
#         if pwd == selected:
#             print(cnt+1)
#         else:
#             cnt += 1
#         return
#     for j in range(len(arr)):
#         selected[level] = arr[j]
#         abc(level+1)
#
# T = int(input())
# password_list = [list(input()) for _ in range(T)]
# for i in range(len(password_list)):
#     pwd = password_list[i]
#     cnt = 0
#     result = abc(0)

# 민코딩 level 30.5 7번
# arr=list(map(int,input().split()))
#
# cnt = 0
#
# def abc(level,start,sum):
#     global cnt
#     if 10<=sum<=20:
#             cnt+=1
#     if level==len(arr):
#         return
#     for i in range(start, len(arr)):
#         abc(level+1, i+1, sum+arr[i])
#
# abc(0,0,0)
# print(cnt)

# 민코딩 level 30.5 8번
# n = int(input())
# heros = ['B', 'I', 'A', 'H']
# index = 0
# for _ in range(4):
#     index -= 1
# n = int(input())
# hero = ['B', 'I', 'A', 'H']
# order = []
#
# for i in range(4):
#     hero_list = []
#     remain_hero = []
#     for j in range(n):
#         hero_list.append(hero[j%(4-i)])
#     target = str(hero_list[n-1])
#     order.append(target)
#
#     for j in range(hero.index(order[-1])+1, hero.index(order[-1])+4-i):
#         remain_hero.append(hero[j%(4-i)])
#     hero = remain_hero
#
# print(*order, sep = ' ')    for i in range(n):
#         index += 1
#     index %= len(heros)
#     print(heros.pop(index), end = ' ')


