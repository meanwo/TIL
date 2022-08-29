# 민코딩 level 30 1번

# arr = [[0, 0, 1, 1, 0, 1], [0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
# n = int(input())
# def dfs(start_node):
#     stack = [start_node]
#     used = []
#
#     # 스택이 비어있지 않다면 반복
#     while stack:
#         node = stack.pop()
#         if node not in used:
#             used.append(node)
#             for i in range(len(arr[node])-1, -1, -1):
#                 if arr[node][i] == 1:
#                     stack.append(i)
#
#     print(*used, sep = ' ')
#
# dfs(n)

# # 민코딩 level 30 2번
# n = int(input())
#
# arr = [[0, 0, 1, 0, 2, 0], [5, 0, 3, 0, 0, 0], [0, 0, 0, 0, 0, 7], [2, 0, 0, 0, 8, 0], [0, 0, 9, 0, 0, 0], [4, 0, 0, 7, 0, 0]]
#
# def dfs(start_node):
#     stack = [start_node]
#     used = []
#     factor = [0]
#     ssum=0
#
#     # 스택이 비어있지 않다면 반복
#     while stack:
#         node = stack.pop()
#         if node not in used:
#             used.append(node)
#             ssum += factor.pop()
#             print(ssum)
#
#             for i in range(len(arr[node])-1, -1, -1):
#                 if arr[node][i] >= 1:
#                     stack.append(i)
#                     if i not in used:
#                         factor.append(arr[node][i])

    # for i in range(1, len(ssum)):
    #     ssum[i] += ssum[i-1]
    # for i in range(len(used)):
    #     print(f'%d %d' %(used[i], ssum[i]))

# dfs(n)


# 민코딩 level 30 3번
# arr = [[0, 1, 0, 0, 1, 0],
#        [0, 0, 1, 0, 0, 1],
#        [0, 0, 0, 1, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0]]
# n = int(input())
#
# def bfs(start_node):
#     queue = [start_node]
#     used = [0]*6
#     used[start_node] = 1
#
#     while queue:
#         node = queue.pop(0)
#         print(node, end = ' ')
#         for i in range(len(arr[node])):
#             if arr[node][i] == 1:
#                 if used[i] == 0:
#                     used[i] = 1
#                     queue.append(i)
#
# bfs(n)

# # 민코딩 level 30 4번
# n = int(input())
# arr = [[0, 0, 0, 0, 1, 0],
#        [1, 0, 1, 0, 0, 1],
#        [1, 0, 0, 1, 0, 0],
#        [1, 1, 0, 0, 0, 0],
#        [0, 1, 0, 1, 0, 1],
#        [0, 0, 1, 1, 0, 0]]
# def bfs(start_node):
#     queue = [start_node]
#     used = [0]*6
#     used[start_node] = 1
#
#     while queue:
#         node = queue.pop(0)
#         print(node)
#         for i in range(len(arr[node])):
#             if arr[node][i] == 1:
#                 if used[i] == 0:
#                     used[i] = 1
#                     queue.append(i)
#
# bfs(n)