T = int(input())

for i in range(T):
    n = int(input())
    color_Info = [list(map(int, input().split())) for _ in range(n)]

    total_place = [[0]*10 for _ in range(10)]


    for j in range(n):
        for k in range(color_Info[j][0], color_Info[j][2]+1):
            for l in range(color_Info[j][1], color_Info[j][3]+1):
                total_place[k][l] += color_Info[j][4]

    purple_cnt = 0
    for j in range(10):
        for k in range(10):
            if total_place[j][k] == 3:
                purple_cnt += 1
    print(f'#%d %d' %(i+1, purple_cnt))