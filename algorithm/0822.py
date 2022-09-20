# dfs 스택코드
# 스택이 빌 때 까지 반복
# def dfs(start_node):
#     stack = [start_node]
#     used = []
#
#     while stack:
#         node = stack.pop()
#         if node not in used:
#             used.append(node)
#             for i in range(len(arr[node])-1, -1, -1):
#                 if arr[node][i] == 1:
#                     stack.append(i)
#     print(used)
#
#
# arr = [
#     [0, 1, 1, 0, 0, 0],
#     [0, 0, 0, 1, 1, 0],
#     [0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0]
# ]
#
# dfs(0)
#

# bfs 코드
# def bfs(start_node):
#     queue = [start_node]
#
#     while queue:
#         node = queue.pop(0)
#         print(node, end=' ')
#         for i in range(len(arr[node])):
#             if arr[node][i] == 1:
#                 queue.append(i)
#
#
# arr = [
#     [0, 1, 1, 0, 0, 0],
#     [0, 0, 0, 1, 1, 0],
#     [0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0]
# ]
#
# bfs(0)

# bfs cycle 대비(used 사용) 코드
# def bfs(start_node):
#     queue = [start_node]
#     used = [0] * 4
#
#     while queue:
#         node = queue.pop(0)
#         print(node, end=' ')
#         for i in range(len(arr[node])):
#             if arr[node][i] == 1:
#                 if used[i] == 0:
#                     used[i] = 1
#                     queue.append(i)
#
#
# arr = [
#     [0, 1, 1, 0],
#     [0, 0, 1, 1],
#     [0, 0, 0, 1],
#     [0, 0, 0, 0]
# ]
#
# bfs(0)

