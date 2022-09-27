#  # 1번
# arr = [list(map(int, input().split())) for _ in range(4)]
# new_list = [[0]*4 for _ in range(4)]
#
# for i in range(1, 4):
#     new_list[0][i] = new_list[0][i-1] + arr[0][i]
#     new_list[i][0] = new_list[i-1][0] + arr[i][0]
#
# for i in range(1, 4):
#     for j in range(1, 4):
#         new_list[i][j] = min(new_list[i][j-1], new_list[i-1][j]) + arr[i][j]
# # print(new_list)
#
# directx = [-1, 0]
# directy = [0, -1]
#
# result = []
# def bfs(y0, x0, y1, x1):
#
#     queue = [(y1, x1, new_list[y1][x1])]
#     while queue:
#         y, x, level = queue.pop(0)
#         result.append((y,x))
#         # print(f'%d,%d' %(y,x))
#
#         if y == y0 and x == x0:
#             break
#
#         dy1 = directy[0] + y
#         dx1 = directx[0] + x
#         dy2 = directy[1] + y
#         dx2 = directx[1] + x
#         part = []
#         if (0<= dy1 < 4 and 0<= dx1 < 4):
#             part.append((dy1, dx1, new_list[dy1][dx1]))
#         if (0<= dy2 < 4 and 0<= dx2 < 4):
#             part.append((dy2, dx2, new_list[dy2][dx2]))
#         part.sort(key = lambda x: x[2])
#         next_y = part[0][0]
#         next_x = part[0][1]
#
#         queue.append((next_y, next_x, part[0][2]))
# bfs(0, 0, 3, 3)
# for i in range(len(result)-1, -1, -1):
#     print(f'%d,%d' %(result[i][0],result[i][1]))

# # 2번
# n = int(input())
# def fivo(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return fivo(n-1)+fivo(n-2)
#
# print(fivo(n))

# # 3번
# arr = list(map(int, input().split()))
# # print(arr)
# new_arr = [0]*12
#
#
# for i in range(2, 12):
#     if i % 2 != 0:
#         new_arr[i] = max(new_arr[i-2], new_arr[i-3]) + arr[i]
#     elif i % 2 == 0:
#         new_arr[i] = max(new_arr[i-2], new_arr[i-3], new_arr[i//2]) + arr[i]
# print(max(new_arr))

# 4번
arr = [list(map(int, input().split())) for _ in range(7)]
new_arr = [[0]*3 for _ in range(7)]

directy = [-1, -1, -1]
directx = [1, 0, -1]
new_arr[0][0] = 1
for i in range(1, 7):
    for j in range(3):
        direct_list = []
        for k in range(3):
            dy = directy[k]+ i
            dx = directx[k] + j
            if not (0 <= dy < 7 and 0 <= dx < 3): continue
            if arr[dy][dx] == 0: continue
            direct_list.append(new_arr[dy][dx])
        # print(direct_list)
        if len(direct_list) != 0:
            new_arr[i][j] = max(direct_list) + arr[i][j]
        else:
            new_arr[i][j] = arr[i][j]

print(max(new_arr[6]))