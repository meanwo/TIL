N = int(input())
arr = [list(input()) for _ in range(N)]
b, a = map(int, input().split())


directy = [1, -1, 0, 0]
directx = [0, 0, 1, -1]

# 소화기 소지 유무
A_have = False

def bfs(y0, x0, y1, x1):
    visited = [[0]*N for _ in range(N)]
    queue = [(y0, x0, 0)]
    visited[y0][x0] = 1
    while queue:
        y, x, level = queue.pop(0)

        if y == y1 and x == x1:
            return level

        for i in range(4):
            dx = directx[i]+x
            dy = directy[i]+y
            if 0 <= dx < N and 0 <= dy < N:
                # 소화기를 가지고 있지 않을 땐 불 좌표에 접근 불가
                if A_have == False and visited[dy][dx] == 0:
                    if arr[dy][dx] != '#' and arr[dy][dx] != '$':
                        visited[dy][dx] = 1
                        queue.append([dy, dx, level+1])
                elif A_have == True and visited[dy][dx] == 0:
                    if arr[dy][dx] != '#':
                        visited[dy][dx] = 1
                        queue.append([dy, dx, level + 1])

# 소화기 좌표와 불 좌표 저장
A_list = []
fire_loc = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'A':
            A_list.append([i, j])
        if arr[i][j] == '$':
            fire_loc = [i, j]


min_cnt = 999
for i in range(len(A_list)):
    cnt1 = bfs(b, a, A_list[i][0], A_list[i][1])
    # 소화기 좌표를 구한 뒤에는 불에 접근 가능하도록 설정
    A_have = True
    cnt2 = bfs(A_list[i][0], A_list[i][1], fire_loc[0], fire_loc[1])
    cnt = cnt1+cnt2

    if min_cnt > cnt:
        min_cnt = cnt
print(min_cnt)
