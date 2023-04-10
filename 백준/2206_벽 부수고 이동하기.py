from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))
# print(arr)

# used 배열이 2개 필요함

# 벽을 한번 부쉈을 때 used 리스트
used_2 = [[0]*M for _ in range(N)]
# 벽을 한번도 부수지 않았을 때 used 리스트
used = [[0]* M for _ in range(N)]

directx = [1, -1, 0, 0]
directy = [0, 0, 1, -1]
cnt = 0

flag = -2
def bfs(N, M):
    global cnt, flag
    q = deque()
    q.append((0, 0, 0, 1))
    used[0][0] = 1
    used_2[0][0] = 1

    while q:
        y, x, cnt, wall = q.popleft()
        if y == N - 1 and x == M - 1:
            flag = cnt
            break

        for i in range(4):
            dy = directy[i]+ y
            dx = directx[i]+ x
            if not(0<= dy <= N-1 and 0<= dx <= M-1): continue
            if wall == 1 and arr[dy][dx] == 1 and used[dy][dx] == 0:
                used[dy][dx] = 1
                q.append((dy, dx, cnt+1, 0))
            elif wall == 1 and arr[dy][dx] == 0 and used[dy][dx] == 0:
                used[dy][dx] = 1
                q.append((dy, dx, cnt+1, 1))
            elif wall == 0 and arr[dy][dx] == 0 and used_2[dy][dx] == 0:
                # if arr[dy][dx] == 0:
                used_2[dy][dx] = 1
                q.append((dy, dx, cnt+1, 0))

    return flag+1


result = bfs(N, M)
print(result)

# bfs(N, M)
# print(cnt)