# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
#
# directy = [1, 1, -1, -1]
# directx = [1, -1, -1, 1]
#
# des_list = []
#
# def dfs(y, x, y0, x0, level, dir):
#     global des_list
#     # if arr[y][x] in des_list:
#     #     return -1
#     # else:
#
#
#     if y == y0 and x == x0:
#         return level
#
#
#     for i in range(2):
#         dy = directy[(i+dir)%4]+y
#         dx = directx[(i+dir)%4]+x
#         backup = des_list
#         if 0 <= dy < N and 0 <= dx < N:
#             des_list.append(arr[dy][dx])
#             dfs(dy, dx, y0, x0, level+1, dir)
#         else:
#             dfs(y, x, y0, x0, level, dir+1)
#         des_list = backup
#
#
# des_list.append(arr[1][2])
# print(dfs(1, 2, 0, 1, 1, 0))
# # for i in range(N-2):
# #     for j in range(1, N-1):
# #         print(dfs(i+1, j+1, i, j, 1, 0))




# n = int(input())
# arr = [list(input()) for _ in range(n)]
#
#
# # 아래, 오른쪽, 대각선 아래를 향한 방향 설정
# directy = [1,0,1,1]
# directx = [0,1,1,-1]
#
#
# def omok(y,x):
#     flag = 0
#     cnt=0 # 함수가 올 때 마다 초기화
#     for i in range(4): # 델타배열 돌면서
#         dy=directy[i]+y # 새로운 y
#         dx=directx[i]+x # 새로운 x
#         if dy<0 or dy>=n or dx<0 or dx>=n: continue # 배열에 벗어나면 무효
#         if arr[dy][dx] == "o" : # O를 찾았다면
#             for j in range(1,4): # 5개만 맞으면 오목임!
#                 new_dy = dy + directy[i]*j # 찾아준 i에 4번 돌아서
#                 new_dx = dx + directx[i]*j
#                 if not (0<= new_dx < n and 0<= new_dy < n): continue
#                 if arr[new_dy][new_dx] == "o": #또 o가 있으면!
#                     cnt += 1
#             if cnt >= 3:
#                 flag = 1
#                 break
#     return flag
#
# # print(omok(0, 4))
# ret_flag = 0
# for i in range(n):
#     for j in range(n): #
#         if arr[i][j] == "o":
#             ret = omok(i,j)
#             # print(ret)
#             if ret==1:
#                 print("Possible")
#                 ret_flag = 1
#                 break
#     if ret_flag == 1:
#         break
#             # else: continue
#
#
# if ret_flag == 0:
#     print("Impossible")