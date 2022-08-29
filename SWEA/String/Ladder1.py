for _ in range(1):
    test_case = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    visit = [[0]*100 for _ in range(100)]
    end = 0
    st_list = []
    for i in range(100):
        if data[0][i] == 1:
            st_list.append(i)

    for i in range(100):
        if data[99][i] == 2:
            end = i

    def dfs(y, x):
        if data[y][x] == 2:
            print(data[y][x])
            print(y, x)
            return
        directx = [-1, 1, 0]
        directy = [0, 0, 1]
        for i in range(3):
            dx = x+directx[i]
            dy = y+directy[i]
            if dx < 0 or dx > 99 or dy <0 or dy >99 : continue
            if visit[dy][dx] == 1: continue
            if data[dy][dx] == 0: continue

            visit[dy][dx] = 1
            dfs(dy, dx)
            visit[dy][dx] = 0

        # visit[y+1][x] = 1
        # dfs(y+1, x)
        # visit[y+1][x] = 0

    dfs(0, 67)
    # for i in range(len(st_list)):
    #     dfs(0, st_list[i])





#     for i in range(100):
#         if data[0][i] == 1:
#             st_list.append(i)
#     for i in range(st_list):
#         while True:
#             for j in range(2):
#                 if row >= 0 and row <= 99 and dx[j]+st_list[i] >= 0 and dx[j]+st_list[i] <= 99:
#                     if data[row][dx[j]+st_list[i]] == 1:


n = int(input())
for m in range(n):
    y1,x1,y2,x2 = map(int,(input().split()))
    arr = [list(map(int,input().split())) for _ in range(n)]

    sum = 0
    avg = 0
    size = (y2-y1+1) * (x2-x1+1) # 넓이

    for i in range(y1,y2+1):
        for j in range(x1,x2+1):
            sum += arr[i][j]

    even_height = sum//size # 평탄화 작업을 위한 높이
    result = 0 # 분산을 구해주기 위한 작업

    for k in range(y1,y2+1):
        for l in range(x1,x2+1):
            if even_height >= arr[k][l]: # abs 를 못 쓰기 때문에 case를 나눠준다.
                result += (even_height - arr[k][l])
            else:
                result += (arr[k][l] - even_height)



    print(result)