# 1번
# arr = list(input())
# new_list = [0]*3
#
# def dfs(level, start):
#     if level == 3:
#         for i in range(3):
#             print(new_list[i], end='')
#         print()
#         return
#     for i in range(start, len(arr)):
#         new_list[level] = arr[i]
#         dfs(level+1, i)
#
# dfs(0, 0)

# 2번
# arr = list(map(int, input().split()))
# max_result = 0
# min_result = 9999
# new_list = [0]*5
# used_list = [0]*5
#
# def dfs(level):
#     global max_result, min_result
#     if level == 5:
#         result = find_result(new_list)
#         if max_result < result:
#             max_result = result
#         if min_result > result:
#             min_result = result
#
#     for i in range(5):
#         if used_list[i] == 0:
#             used_list[i] = 1
#             new_list[level] = arr[i]
#             dfs(level+1)
#             used_list[i] = 0
#
# def find_result(lst):
#     result = lst[0]*lst[1] - lst[2]*lst[3] + lst[4]
#     return result
#
#
# dfs(0)
# print(max_result)
# print(min_result)

# 3번
# arr = ['BTS', 'SBS', 'BS', 'CBS', 'SES']
# sentence = input()
#
# min_cnt = 999
# def dfs(level, result, cnt):
#     global min_cnt
#     if len(result) >= len(sentence):
#         if min_cnt > cnt:
#             min_cnt = cnt
#         return
#     for i in range(5):
#         backup = result
#         dfs(level+1, result+arr[i], cnt+1)
#         result = backup
#
# dfs(0, '', 0)
# print(min_cnt)

# 4번
# coin_list = [10, 40, 60]
# change = int(input())
# min_cnt = 9999
# def dfs(level, change, cnt):
#     global coin_list, min_cnt
#     if change <= 0:
#         if cnt < min_cnt:
#             min_cnt = cnt
#         return
#
#     for i in range(len(coin_list)):
#         backup = change
#         dfs(level+1, change-coin_list[i], cnt+1)
#         change = backup
#
# dfs(0, change, 0)
# print(min_cnt)

# 5번
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# N = int(input())
#
# cnt = 0
# def dfs(level, total):
#     global cnt
#     if level == N:
#         if total == 10:
#             cnt += 1
#         return
#
#     for i in range(9):
#         backup = total
#         dfs(level+1, total+num_list[i])
#         total = backup
# dfs(0, 0)
# print(cnt)

# 6번
N, M = map(int, input().split())
arr = list(map(int, input().split()))

used_list = [0]*N
new_list = [0]*M
min_result = 999
min_list = []
def dfs(level, result):
    global min_result, min_list
    if level == M:
        if result < min_result:
            min_list = new_list
            min_result = result
        return

    for i in range(N):
        if used_list[i] == 0:
            used_list[i] = 1
            new_list[level] = arr[i]
            backup = result
            dfs(level+1, result*arr[i])
            used_list[i] = 0
            result = backup
a = dfs(0, 1)
# print(a)
print(min_result)
print(min_list)