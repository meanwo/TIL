# directx = [0, 0, 1, -1]
# directy = [1, -1, 0, 0]
#
# arr = [[0, 0, 0, 1, 1],
#        [0, 0, 0, 1, 0],
#        [1, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0]]
#
#
# answer = 0
# def bfs(x1, y1, x2, y2):
#     queue = [(y1, x1, 0)]
#     used = [[0]*5 for _ in range(4)]
#     used[y1][x1] = 1
#     while queue:
#         node = queue.pop(0)
#         y, x, level = node[0], node[1], node[2]
#         if y == y2 and x == x2:
#             return level
#
#         for k in range(4):
#             dx = directx[k]+x
#             dy = directy[k]+y
#             if 0 <= dx < 5 and 0 <= dy < 4:
#                 if used[dy][dx] == 0 and arr[dy][dx] == 0:
#                     used[dy][dx] = 1
#                     queue.append((dy, dx, level+1))
#
# answer += bfs(0, 0, 0, 3)
# answer += bfs(0, 3, 4, 3)
# print(answer)


# 섬의 크기를 구하는 문제
# arr = [[0, 0, 1, 0, 0],
#       [0, 0, 1, 0, 0],
#       [0, 1, 1, 1, 0],
#       [0, 0, 1, 0, 0],
#       [0, 0, 0, 0, 0]]
#
# directx = [0, 0, 1, -1]
# directy = [1, -1, 0, 0]
#
# used = [[0]*5 for _ in range(5)]
#
# def bfs(y, x):
#     queue = [(y, x)]
#     # used[y][x] = 1
#     size = 1
#     while queue:
#         node = queue.pop(0)
#         yy, xx = node[0], node[1]
#         for k in range(4):
#             dx = directx[k]+xx
#             dy = directy[k]+yy
#             if 0 <= dx < 5 and 0 <= dy < 5:
#                 if used[dy][dx] == 0 and arr[dy][dx] == 1:
#                     queue.append([dy, dx])
#                     used[dy][dx] = 1
#                     size += 1
#     return size
#     # return
#
# # print(bfs(2,0))
# #
# #
# for y in range(5):
#     for x in range(5):
#         if arr[y][x] == 1 and used[y][x] == 0:
#             used[y][x] = 1
#             print(bfs(y,x))

# 섬의 크기를 구하는 문제(used 안사용하는 방식)

# from collections import deque
#
# Map = [
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0]
# ]
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# def bfs(y, x):
#     q = deque()
#     q.append([y, x])
#     size = 0
#     while q:
#         y, x = q.popleft()
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0 <= ny < 5 and 0 <= nx < 5:
#                 if Map[ny][nx] == 1:
#                     q.append([ny, nx])
#                     Map[ny][nx] = 0
#                     size += 1
#     return size
#
#
# for y in range(5):
#     for x in range(5):
#         if Map[y][x] == 1:
#             print(bfs(y, x))
# 각각 섬의 크기 구하기
# from collections import deque
#
# def bfs(y, x):
#     global visited
#     q = deque()
#     q.append([y, x])
#     size = 0
#     while q:
#         size += 1 # 섬 크기 size+1
#         now = q.popleft()
#         y, x = now
#         dy = [0,1,0,-1]
#         dx = [1,0,-1,0]
#         for i in range(4):
#             ny, nx = y+dy[i], x+dx[i]
#             if ny > N-1 or nx > N-1 or ny< 0 or nx < 0: continue
#             if visited[ny][nx] == 1: continue
#             if arr[ny][nx]==0: continue
#             visited[ny][nx] = 1
#             q.append([ny, nx])
#     return size
#
#
#
# arr = [ # 1: 섬 | 0: 바다
#     [0,0,1,0,0],
#     [0,0,1,0,0],
#     [0,1,1,1,0],
#     [0,0,1,0,0],
#     [1,0,0,0,1],
# ]
# N = len(arr) # int(input())
#
# cnt = 0
# visited = [[0]*N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if arr[i][j]==1 and visited[i][j]==0:
#             visited[i][j] = 1   # 중복체크 해주고
#             cnt+=1 # 섬의 갯수 +1
#             print(f'{cnt}번 째 섬 크기 : {bfs(i, j)}')
# print(f'섬의 총 갯수 : {cnt}')


# 위상정렬
# from collections import deque
#
# name=['cs','language','datastructure','algorithm','project','codingtest','to be a programmer']
#
# arr = [
#     [0,0,0,0,0,0,1],
#     [0,0,1,1,1,0,0],
#     [0,0,0,0,0,1,0],
#     [0,0,0,0,0,1,0],
#     [0,0,0,0,0,0,1],
#     [0,0,0,0,0,0,1],
#     [0,0,0,0,0,0,0],
# ]
#
# acc=[0]*7
# used=[0]*7
#
# q = deque()
# for j in range(7):          # 사전 작업 개수 등록
#     for i in range(7):
#         if arr[i][j]==1:
#             acc[j]+=1
#
# for i in range(7):          # 바로 작업 착수 가능한 것들은
#     if acc[i]==0:           # used에 1체크 하고 q에 등록
#         used[i]=1
#         q.append(i)
#
# while q:
#     now = q.popleft()
#     print(name[now])
#
#     for i in range(7):
#         if arr[now][i]==1 and used[i]==0:
#             if acc[i]==1:
#                 used[i]=1
#                 acc[i]-=1
#                 q.append(i)
#             else:
#                 acc[i]-=1

# 벽을 두 번 부술 수 있을 때, 왕자를 구할 수 있는 최소 이동횟수 구하기

# arr = [list(map(int, input().split())) for _ in range(4)]
# arr = [
#     [0, 0, 1, 1, 1, 1],
#     [0, 0, 1, 0, 0, 1],
#     [0, 0, 1, 0, 0, 1],
#     [0, 1, 1, 1, 1, 0]
# ]
#
# directx = [0, 0, 1, -1]
# directy = [1, -1, 0, 0]
#
# answer = 0
# def bfs(x1, y1, x2, y2):
#     queue = [(y1, x1, 0, 2)]
#     used = [[0]*6 for _ in range(4)]
#     used[y1][x1] = 1
#     while queue:
#         node = queue.pop(0)
#         y, x, level, break_wall = node[0], node[1], node[2], node[3]
#         if y == y2 and x == x2:
#             # print(level)
#             return level
#
#         for k in range(4):
#             dx = directx[k]+x
#             dy = directy[k]+y
#             if 0 <= dx < 6 and 0 <= dy < 4:
#                 if used[dy][dx] == 0:
#                     if arr[dy][dx] == 0:
#                         used[dy][dx] = 1
#                         queue.append((dy, dx, level+1, break_wall))
#                     else:
#                         if break_wall > 0:
#                             used[dy][dx] = 1
#                             queue.append((dy, dx, level+1, break_wall))
#
# answer += bfs(0, 0, 5, 3)
# print(answer)