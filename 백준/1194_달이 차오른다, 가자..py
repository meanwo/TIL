import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(list(input()))

# 비트마스킹
used = [[[0]*64 for _ in range(M)] for _ in range(N)]
directy = [1, -1, 0, 0]
directx = [0, 0, 1, -1]
key_list = ['a', 'b', 'c', 'd', 'e', 'f']
door_list = ['A', 'B', 'C', 'D', 'E', 'F']

key_state = {'a': 32, 'b': 16, 'c': 8, 'd': 4, 'e': 2, 'f': 1}
door_state = {'A': 32, 'B': 16, 'C': 8, 'D': 4, 'E': 2, 'F': 1}


# 시작 좌표 구하기
st_y = 0
st_x = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '0':
            st_y = i
            st_x = j

flag = -1
my_key = []
def bfs(st_y, st_x):
    global used, flag
    q = deque()
    q.append([st_y, st_x, 0, -1])
    used[st_y][st_x][0] = 1
    while q:
        y, x, my_key, cnt = q.popleft()
        if arr[y][x] == '1':
            flag = cnt+1
            break
        for i in range(4):
            dy = directy[i] + y
            dx = directx[i] + x
            if not (0 <= dy <= N-1 and 0 <= dx <= M-1): continue
            if used[dy][dx][my_key] != 0: continue
            if arr[dy][dx] == '#': continue

            if arr[dy][dx] in key_list:
                # 새로운 키를 얻었을 때 키를 new_key로 갱신
                if my_key & key_state[arr[dy][dx]] == 0:
                    new_key = my_key + key_state[arr[dy][dx]]
                    # print(new_key)
                    used[dy][dx][new_key] = 1
                    q.append([dy, dx, new_key, cnt+1])
                else:
                    used[dy][dx][my_key] = 1
                    q.append([dy, dx, my_key, cnt+1])
            elif arr[dy][dx] in door_list and (my_key & door_state[arr[dy][dx]]):
                used[dy][dx][my_key] = 1
                q.append([dy, dx, my_key, cnt+1])
            elif arr[dy][dx] in ['.', '0', '1']:
                used[dy][dx][my_key] = 1
                q.append([dy, dx, my_key, cnt+1])


    return flag

result = bfs(st_y, st_x)
print(result)


