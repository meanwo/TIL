directy = [1, 1]
directx = [1, -1]

# 이동 횟수 2*(i+j)의 최댓값은 y좌표 크기에 반비례

def cnt_cafe(y, x, max_length):
    # i 는 우하단, 좌상단 이동횟수
    for i in range(N-1-x, 0, -1):
        # j는 좌하단, 우상단 이동횟수
        area = min(x, N-i-y-1)
        for j in range(area, 0, -1):
            flag = 1
            cafe_list = []
            dy = y
            dx = x
            for k in range(1, -3, -2):
                for l in range(1, i+1):
                    dy = directy[0] * k + dy
                    dx = directx[0] * k + dx
                    if arr[dy][dx] in cafe_list:
                        cafe_list = []
                        flag = 0
                        break
                    else:
                        cafe_list.append(arr[dy][dx])
                if flag == 0:
                    break
                for l in range(1, j+1):
                    dy = directy[1] * k + dy
                    dx = directx[1] * k + dx
                    if arr[dy][dx] in cafe_list:
                        cafe_list = []
                        flag = 0
                        break
                    else:
                        cafe_list.append(arr[dy][dx])
                if flag == 0:
                    break
            if len(cafe_list) != 0:
                if max_length < len(cafe_list):
                    max_length = len(cafe_list)
    return max_length


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_lenth = -1
# 이동 횟수 2*(i+j)의 최댓값은 y좌표 크기에 반비례
    max_cnt = -1
    for i in range(N-2):
        for j in range(1, N-1):
            # print(cnt_cafe(i, j))
            if cnt_cafe(i, j, -1) > max_cnt:
                max_cnt = cnt_cafe(i, j, -1)

    print(f'#%d %d' %(test_case, max_cnt))




















