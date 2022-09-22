# 1번
# N = int(input())
# y1, x1, y2, x2 = map(int, input().split())
# virus = [(y1, x1, 1), (y2, x2, 1)]
# arr = [[0]*N for _ in range(N)]
# directx = [-1, 1, 0, 0]
# directy = [0, 0, 1, -1]
#
# def bfs(virus):
#
#
#     while virus:
#         y, x, level = virus.pop(0)
#         arr[y][x] = level
#
#         for i in range(4):
#             dy = y+directy[i]
#             dx = x+directx[i]
#             if not (0<= dy <N and 0<= dx < N): continue
#             if arr[dy][dx] != 0: continue
#             arr[dy][dx] = arr[y][x]+1
#             virus.append((dy, dx, level+1))
#
# bfs(virus)
#
# for i in range(N):
#     print(*arr[i], sep='')

# 2번
# Y, X = map(int, input().split())
# arr = [list(input().split()) for _ in range(Y)]
#
# y0, x0 = map(int, input().split())
# queue = [(y0, x0, 0)]
# directx = [-1, 1, 0, 0]
# directy = [0, 0, 1, -1]
# def bfs(queue):
#
#     while queue:
#         y, x, level = queue.pop(0)
#         arr[y][x] = level
#         for i in range(4):
#             dy = y + directy[i]
#             dx = x + directx[i]
#             if not(0 <= dy < Y and 0 <= dx < X): continue
#             if arr[dy][dx] != '0': continue
#             arr[dy][dx] = int(arr[y][x]) + 1
#             queue.append((dy, dx, level+1))
#
# bfs(queue)
# max_cnt = 0
# for i in range(Y):
#     for j in range(X):
#         arr[i][j] = int(arr[i][j])
#
# # print(arr)
# for i in range(Y):
#     for j in range(X):
#         if arr[i][j] > max_cnt:
#             max_cnt = arr[i][j]
#
# print(max_cnt)

# 3번
# arr = [list(map(int, input().split())) for _ in range(4)]
#
# firework_list = []
#
# for i in range(4):
#     for j in range(5):
#         if arr[i][j] == 1:
#             firework_list.append([i, j, 0])
#
# directx = [0, 0, 1, -1, -1, -1, 1, 1]
# directy = [1, -1, 0, 0, -1, 1, -1, 1]
# level = 0
# def bfs(firework_list):
#     global level
#     while firework_list:
#         y, x, level = firework_list.pop(0)
#         arr[y][x] = 1
#         for i in range(8):
#             dy = y + directy[i]
#             dx = x + directx[i]
#             if not(0 <= dy < 4 and 0 <= dx < 5) : continue
#             if arr[dy][dx] != 0: continue
#             arr[dy][dx] = 1
#             firework_list.append((dy, dx, level+1))
#
# bfs(firework_list)
# print(level)

# 4번
# arr = [list(map(int, input().split())) for _ in range(4)]
#
# used_list = [[0]*4 for _ in range(4)]
# directy = [1, -1, 0, 0]
# directx = [0, 0, 1, -1]
#
# def bfs(y0, x0):
#     queue = [(y0, x0)]
#     size = 0
#     while queue:
#         y, x = queue.pop(0)
#         for i in range(4):
#             dy = directy[i]+y
#             dx = directx[i]+x
#             if not (0 <= dy < 4 and 0 <= dx < 4): continue
#             if arr[dy][dx] == 0: continue
#             if used_list[dy][dx] == 1: continue
#             used_list[dy][dx] = 1
#             queue.append((dy, dx))
#             size += 1
#     return size
#
# print(bfs(0, 0))

# 5번
# arr = [[0, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [1, 0, 1, 0]]
# y1, x1 = map(int, input().split())
# y2, x2 = map(int, input().split())
# used_list = [[0]*4 for _ in range(4)]
# directy = [1, -1, 0, 0]
# directx = [0, 0, 1, -1]
#
# def bfs(y1, x1, y2, x2):
#     queue = [(y1, x1, 0)]
#     used_list[y1][x1] = 1
#
#     while queue:
#         y, x, level = queue.pop(0)
#         if y == y2 and x == x2:
#             print(f'%d회' %level)
#         for i in range(4):
#             dy = directy[i]+ y
#             dx = directx[i]+ x
#             if not(0<=dy<4 and 0<=dx<4): continue
#             if arr[dy][dx] == 1: continue
#             if used_list[dy][dx] == 1: continue
#             used_list[dy][dx] = 1
#             queue.append((dy, dx, level+1))
#
#
# bfs(y1, x1, y2, x2)

# 6번
# arr = [list(map(int, input().split())) for _ in range(4)]
# directy = [0, 0, 1, -1]
# directx = [1, -1, 0, 0]
# used_list = [[0]*6 for _ in range(4)]
#
# def bfs(y0, x0):
#     global cnt
#     cnt = 0
#     queue = [(y0, x0)]
#     used_list[y0][x0] = 1
#
#     while queue:
#
#         y, x = queue.pop(0)
#
#         if arr[y][x] == 2:
#             cnt += 1
#         for i in range(4):
#             dy = directy[i] + y
#             dx = directx[i] + x
#             if not(0 <= dy < 4 and 0 <= dx < 6): continue
#             if arr[dy][dx] == 1: continue
#             if used_list[dy][dx] == 1: continue
#             used_list[dy][dx] = 1
#             queue.append([dy, dx])
# bfs(0, 0)
#
# print(cnt)

# 7번
# N, M = map(int, input().split())
#
# arr = [list(input().split()) for _ in range(N)]
# directy = [1, -1, 0, 0]
# directx = [0, 0, 1, -1]
#
# def bfs(y0, x0, y1, x1):
#
#     used_list = [[0]*M for _ in range(N)]
#     queue = [(y0, x0, 0)]
#     while queue:
#         y, x, level = queue.pop(0)
#
#         if y == y1 and x == x1:
#             # print(level)
#             return level
#         for i in range(4):
#             dy = directy[i] + y
#             dx = directx[i] + x
#
#             if not (0 <= dy < N and 0 <= dx < M): continue
#             if used_list[dy][dx] == 1: continue
#             if arr[dy][dx] != 'x' and arr[dy][dx] != 'X':
#                 used_list[dy][dx] = 1
#                 queue.append([dy, dx, level+1])
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 'S':
#             y0, x0 = i, j
#         elif arr[i][j] == 'C':
#             y1, x1 = i, j
#         elif arr[i][j] == 'D':
#             y2, x2 = i, j
# result = 0
#
# result += bfs(y0, x0, y1, x1)
# result += bfs(y1, x1, y2, x2)
# print(result)

# 8번
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# directy = [1, -1, 0, 0]
# directx = [0, 0, 1, -1]
# used_list = [[0] * M for _ in range(N)]
# def bfs(y0 ,x0):
#     global used_list
#     queue = [(y0, x0)]
#     while queue:
#         y, x = queue.pop(0)
#         for i in range(4):
#             dy = directy[i] + y
#             dx = directx[i] + x
#
#             if not(0<= dy < N and 0<= dx<M): continue
#             if used_list[dy][dx] == 1: continue
#             if arr[dy][dx] == 0: continue
#             used_list[dy][dx] = 1
#             queue.append([dy, dx])
#
# cnt = 0
# used_list = [[0] * M for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1 and used_list[i][j] == 0:
#             used_list[i][j] = 1
#             bfs(i, j)
#             cnt+=1
#
# print(cnt)