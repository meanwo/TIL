# 1번
# arr = [0]*1000001
#
# S = int(input())
# D = int(input())
#
#
# def bfs(S, D):
#     queue = [(S, 0)]
#
#
#     while queue:
#         x, level = queue.pop(0)
#
#         if x == D:
#             return level
#         for i in range(4):
#             if i == 0:
#                 dx = x//2
#             elif i == 1:
#                 dx = x*2
#             elif i == 2:
#                 dx = x+1
#             elif i == 3:
#                 dx = x-1
#             if not 0 < dx <= 100000: continue
#             if arr[dx] == 1: continue
#             arr[dx] = 1
#             queue.append((dx, level+1))
# result = bfs(S, D)
# print(result)

# 2번
arr = [list(map(int, input().split())) for _ in range(4)]
