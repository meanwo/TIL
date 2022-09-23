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
# arr = [list(map(int, input().split())) for _ in range(4)]
# used_list = [[0]*9 for _ in range(4)]
# directy = [1, -1, 0, 0]
# directx = [0, 0, 1, -1]
#
#
# def bfs(y0, x0):
#     size = 0
#     global used_list
#     queue = [(y0, x0)]
#     spec = arr[y0][x0]
#     while queue:
#         size += 1
#         y, x = queue.pop(0)
#
#         for i in range(4):
#             dy = directy[i] + y
#             dx = directx[i] + x
#             if not (0 <= dy < 4 and 0 <= dx < 9): continue
#             if used_list[dy][dx] == 1: continue
#             if arr[dy][dx] == spec:
#                 used_list[dy][dx] = 1
#                 queue.append((dy, dx))
#     return [spec, size]
#
# spec_size_list = []
# for i in range(4):
#     for j in range(9):
#         if used_list[i][j] == 0:
#             used_list[i][j] = 1
#             spec_size_list.append(bfs(i, j))
#
# # print(spec_size_list)
#
# spec_size_list.sort(key= lambda x: -x[1])
#
# print(spec_size_list[0][0]*spec_size_list[0][1])


# 3번
# arr = [list(map(int, input())) for _ in range(7)]
# directy = [1, -1, 0, 0]
# directx = [0, 0, 1, -1]
# used_list = [[0]* 7 for _ in range(7)]
#
# def bfs(y0, x0, target):
#     used_list = [[0]* 7 for _ in range(7)]
#     flag = 0
#     queue = [(y0, x0, 0)]
#     used_list[y0][x0] = 1
#     while queue:
#         y, x, level = queue.pop(0)
#         if arr[y][x] == target and level <= target+2 and (y != y0 or x != x0):
#             flag = 1
#             break
#         # elif arr[y][x] == target and level > 3:
#         #     flag = 0
#         for i in range(4):
#             dy = directy[i] + y
#             dx = directx[i] + x
#             if not (0<= dy < 7 and 0<= dx < 7): continue
#             if used_list[dy][dx] == 1: continue
#             used_list[dy][dx] = 1
#             queue.append((dy, dx, level+1))
#     return flag
#
# result = 1
# for i in range(7):
#     for j in range(7):
#         if arr[i][j] == 1:
#             used_list = [[0]* 7 for _ in range(7)]
#             result *= bfs(i, j, 1)
#         elif arr[i][j] == 2:
#             used_list = [[0]* 7 for _ in range(7)]
#             result *= bfs(i, j, 1)
#
# if result == 1:
#     print('pass')
# else:
#     print('fail')

# 4번
# arr = [list(input()) for _ in range(8)]
# directy = [1, -1, 0, 0]
# directx = [0, 0, 1, -1]
# used_list = [[0]*9 for _ in range(8)]
#
# def bfs(y0, x0, cnt):
#     global used_list
#
#     used_list[y0][x0] = 1
#     arr[y0][x0] = cnt
#     queue = [(y0, x0)]
#     while queue:
#         y, x = queue.pop(0)
#         for i in range(4):
#             dy = directy[i] + y
#             dx = directx[i] + x
#             if not(0 <= dy < 8 and 0 <= dx < 9):continue
#             if used_list[dy][dx] == 1: continue
#             if arr[dy][dx] == '_': continue
#             used_list[dy][dx] = 1
#             arr[dy][dx] = cnt
#             queue.append((dy, dx))
#
# def find_lenth(y0, x0):
#     used_list = [[0]*9 for _ in range(8)]
#     used_list[y0][x0] = 1
#     queue = [(y0, x0, 0)]
#     while queue:
#         y, x, level = queue.pop(0)
#         if arr[y][x] == 1:
#             break
#         for i in range(4):
#             dy = directy[i] + y
#             dx = directx[i] + x
#             if not(0 <= dy < 8 and 0 <= dx < 9):continue
#             if used_list[dy][dx] == 1: continue
#             # if arr[dy][dx] != '_': continue
#             used_list[dy][dx] = 1
#             queue.append((dy, dx, level+1))
#     return level
# cnt = 0
# for i in range(8):
#     for j in range(9):
#         if arr[i][j] == '#':
#             cnt += 1
#             bfs(i, j, cnt)
# # print(arr)
#
# min_length = 999
# used_list = [[0]*9 for _ in range(8)]
# for i in range(8):
#     for j in range(9):
#         if arr[i][j] == 2:
#             length = find_lenth(i, j)
#             if min_length > length:
#                 min_length = length
# print(min_length-1)

# 6번
Y, X = map(int, input().split())
arr = [list(input()) for _ in range(Y)]
directy = [1, -1, 0, 0]
directx = [0, 0, 1, -1]

cnt = 0
def bfs(y0, x0, target):
    queue = [(y0, x0, 0)]
    used_list = [[0]*X for _ in range(Y)]
    used_list[y0][x0] = 1
    while queue:
        y, x, level = queue.pop(0)
        if arr[y][x] == target:
            break
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if not (0 <= dx < X and 0 <= dy < Y): continue
            if used_list[dy][dx] == 1: continue
            if arr[dy][dx] == '#': continue
            used_list[dy][dx] = 1
            queue.append((dy, dx, level+1))
    return [y, x, level]



first = bfs(0, 0, '1')
second = bfs(first[0], first[1], '2')
third = bfs(second[0], second[1], '3')
fourth = bfs(third[0], third[1], '4')
print(first[2]+second[2]+third[2]+fourth[2], end = '')
print('회')




