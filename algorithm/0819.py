
# 1. 배열 전체 평균 구하기
# 각 좌표값과 배열평균과의 차이의 합 출력하기
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
#
# # 2 4 7 4 2
# # 2 9 5 3 1
# # 4 9 6 5 3
# # 3 7 9 2 3
# # 1 1 2 3 4
#
# sum_arr = [0]*5
# avr_arr = [0]*5
# for i in range(5):
#     for j in range(5):
#         sum_arr[i] += arr[i][j]
#     avr_arr[i] = sum_arr[i]//5
#
#
# print(avr_arr)
# diff_arr = [0]*5
#
# for i in range(5):
#     for j in range(5):
#         diff_arr[i] += avr_arr[i]-arr[i][j]
#
# # 결과값 출력
# print(diff_arr)
# 1 1 1 1
# 1 0 1 1
# 1 1 1 1
# 1 1 0 1
# 1 0 1 1

# 2. check_arr 이 arr 에 얼마나 포함되어있는지 카운트하기
# a, b = list(map(int, input().split()))
# arr = [list(map(int, input().split())) for _ in range(a)]
# # print(arr)
#
# check_arr = [[1, 1], [1, 0]]
# cnt = 0
#
# for i in range(a-1):
#     for j in range(b-1):
#         flag = 0
#         for k in range(2):
#             for l in range(2):
#                 if arr[i+k][j+l] == check_arr[k][l]:
#                     flag += 1
#                 else:
#                     flag = 0
#                     break
#         if flag ==4:
#             cnt+= 1
#
# print(cnt)
# 3. 산봉우리를 구하는 문제
# n, m = list(map(int, input().split()))
# arr = [list(map(int, input().split())) for _ in range(n)]
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# # 2 4 2 1 5
# # 1 2 1 4 3
# # 2 2 2 4 2
# # 1 7 3 2 3
#
# for i in range(n):
#     for j in range(m):
#         flag = 1
#         cnt = 0
#         for k in range(4):
#             if dy[k]+i >= 0 and dy[k]+i <= n and dx[k]+j >= 0 and dx[k]+j <= m:
#                 if arr[i][j] > arr[i+dy[k]][j+dx[k]]:
#                     print(i, j)
#                     flag = 0
#                     break
#     if flag == 1:
#         cnt += 1
# print(cnt)

# 4. dfs 문제 층별로 숫자의 합을 더해 max를 구하는 문제

# arr = [
#     [2, 5, 7],
#     [8, 4, -8],
#     [-7, 1, 4],
#     [5, 1, 9]
# ]
# max = 0
# def dfs(level, sum):
#     global max
#     if level == 4:
#         if max < sum:
#             max = sum
#             # print(max)
#         return
#     for i in range(3):
#         dfs(level+1, sum+arr[level][i])
#
# result = dfs(0, 0)
# result
# print(max)

# 5. 4의 심화문제
# arr = [[3, 2, 4, 1],
#        [0, 1, 0, 5],
#        [2, 0, 3, 0],
#        [5, 4, 0, 2],
#        [2, -5, 0, 3]]
#
# max = 0
# before_index = [0]*5
# def dfs(level, sum):
#     global max
#     if level == 5:
#         if max < sum:
#             max = sum
#             # print(max)
#         return
#     for i in range(4):
#         if level > 0 and abs(before_index[level-1]-i) >= 2 : continue
#         if arr[i] == 0: continue
#         before_index[level] = i
#         dfs(level + 1, sum + arr[level][i])
#
# result = dfs(0, 0)
# result
# print(max)

# 6. 미로 경로 출력 문제
# arr = [[0, 0, 0, 0],
#        [1, 0, 1, 0],
#        [1, 0, 1, 0],
#        [0, 0, 0, 0]]
#
# visit = [[0]*4 for _ in range(4)]
# flag = 0
#
# visit[0][0] = 1
# def dfs(y, x):
#     global flag
#     if y == 3 and x == 3:
#         flag = 1
#         return
#
#     directy = [-1, 1, 0, 0]
#     directx = [0, 0, -1, 1]
#     for i in range(4):
#         dy = y+directy[i]
#         dx = x+directx[i]
#
#         if dy < 0 or dx < 0 or dy > 3 or dx > 3: continue
#         if visit[dy][dx] == 1: continue
#         if arr[dy][dx] == 1: continue
#         visit[dy][dx] =1
#         dfs(dy,dx)
#         # if flag == 1:
#         #     return
# dfs(0, 0)
# if flag == 1:
#     print("갈수 있어~~")
# else:
#     print("도착할 수 없음")


# 7. 미로찾기(dfs) 최단거리 출력

# arr = [[0, 0, 0, 0, 1],
#        [1, 0, 1, 0, 1],
#        [1, 0, 1, 0, 1],
#        [0, 0, 0, 0, 0]]
#
# visit = [[0]*5 for _ in range(4)]
# flag = 0
#
# visit[0][0] = 1
# min_cnt = 999
# def dfs(y, x, cnt):
#     global min_cnt
#     if y == 1 and x == 3:
#         if min_cnt > cnt:
#             min_cnt = cnt
#         return
#     directy = [-1, 1, 0, 0]
#     directx = [0, 0, -1, 1]
#
#
#     for i in range(4):
#         dy = y+directy[i]
#         dx = x+directx[i]
#         if dy < 0 or dx < 0 or dy > 3 or dx > 4: continue
#         if visit[dy][dx] == 1: continue
#         if arr[dy][dx] == 1: continue
#         visit[dy][dx] = 1
#         dfs(dy, dx, cnt+1)
#         visit[dy][dx] = 0
# dfs(0, 0, 0)
# print(min_cnt)

# 3. 산봉우리를 구하는 문제
# n, m = list(map(int, input().split()))
# arr = [list(map(int, input().split())) for _ in range(n)]
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# # 2 4 2 1 5
# # 1 2 1 4 3
# # 2 2 2 4 2
# # 1 7 3 2 3
#
# cnt = 0
# for i in range(n):
#     for j in range(m):
#         flag = 1
#         for k in range(4):
#             if (dy[k]+i >= 0 and dy[k]+i < n) and (dx[k]+j >= 0 and dx[k]+j < m):
#                 if arr[i][j] <= arr[i+dy[k]][j+dx[k]]:
#                     print(i, j)
#                     flag = 0
#                     break
#         if flag == 1:
#             cnt += 1
# print(cnt)
#
#
# a, b = map(int,input().split())
# arr = [list(map(int,input().split())) for i in range(a)]
#
#
# def Map(y,x):
#     directy = [-1,1,0,0]
#     directx = [0,0,-1,1]
#     for i in range(4):
#         dy = directy[i] + y
#         dx = directx[i] + x
#         if dy < 0 or dx < 0 or dy > 3 or dx >4:
#             continue
#         if arr[y][x] <= arr[dy][dx]:
#             return 0
#     return 1
#
#
#
#
# ret = 0
# for i in range(4):
#     for j in range(5):
#         ret += Map(i,j)
# print(ret)