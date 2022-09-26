N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

directy = [1, 1, -1, -1]
directx = [1, -1, -1, 1]

des_list = []

def dfs(y, x, y0, x0, level, dir):
    global des_list
    # if arr[y][x] in des_list:
    #     return -1
    # else:


    if y == y0 and x == x0:
        return level

    for j in range(4):
        if dir == j:
            for i in range(2):
                dy = directy[(i+dir)%4]+y
                dx = directx[(i+dir)%4]+x
                backup = des_list
                if 0 <= dy < N and 0 <= dx < N:
                    des_list.append(arr[dy][dx])
                    dfs(dy, dx, y0, x0, level+1, dir)
                else:
                    dfs(y, x, y0, x0, level, dir+1)
                des_list = backup


des_list.append(arr[1][2])
print(dfs(1, 2, 0, 1, 1, 0))
# for i in range(N-2):
#     for j in range(1, N-1):
#         print(dfs(i+1, j+1, i, j, 1, 0))
