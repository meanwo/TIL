R, C, T = map(int, (input().split()))
arr = [[] for _ in range(R)]
for i in range(R):
    arr[i]= list(map(int, input().split()))


# 우, 좌, 하, 상
directx = [1, -1, 0, 0]
directy = [0, 0, 1, -1]


new_arr = [[0] * C for _ in range(R)]
air_con = []
for i in range(R):
    if arr[i][0] == -1:
        air_con.append(i)
# print(arr)
while T:

    # 확산 부분
    new_arr = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            count = 0
            idx_list = []
            if arr[i][j] == 0 or arr[i][j] == -1: continue
            for k in range(4):
                di = directy[k]+i
                dj = directx[k]+j
                if not (0 <= di < R and 0 <= dj < C): continue
                if arr[di][dj] == -1: continue
                count += 1
                idx_list.append(k)

            for k in idx_list:
                di2 = directy[k]+i
                dj2 = directx[k]+j
                if arr[di2][dj2] == -1: continue
                new_arr[di2][dj2] += arr[i][j]//5
            new_arr[i][j] += arr[i][j]-count*(arr[i][j]//5)
    # arr = new_arr
    # print(new_arr)
    # # 공기청정기 작동 부분
    new_arr2 = [[0] * C for _ in range(R)]
    for i in range(1, C):
        new_arr2[0][C-i-1] = new_arr[0][C-i]
        new_arr2[R-1][C-i-1] = new_arr[R-1][C-i]
        new_arr2[air_con[0]][i] = new_arr[air_con[0]][i-1]
        new_arr2[air_con[1]][i] = new_arr[air_con[1]][i-1]
    for i in range(1, R):
        if i <= air_con[0]:
            new_arr2[i][0] = new_arr[i-1][0]
            new_arr2[i-1][C-1] = new_arr[i][C-1]
        if i > air_con[1]:
            new_arr2[i-1][0] = new_arr[i][0]
            new_arr2[i][C-1] = new_arr[i-1][C-1]
    new_arr2[air_con[0]][0] = -1
    new_arr2[air_con[1]][0] = -1

    for i in range(R):
        for j in range(C):
            if i == 0 or i == R-1 or j == 0 or j == C-1 or i == air_con[0] or i == air_con[1]:
                arr[i][j] = new_arr2[i][j]
            else:
                arr[i][j] = new_arr[i][j]
    T -= 1


result = 0
for i in range(R):
    for j in range(C):
        result+= arr[i][j]
# print(arr)
print(result+2)