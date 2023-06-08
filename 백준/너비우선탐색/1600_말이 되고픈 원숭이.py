from collections import deque
import sys
input = sys.stdin.readline

# K = int(input())
K = int(sys.stdin.readline())
# W, H = map(int, input().split())
W, H = map(int, sys.stdin.readline().split())
arr = []
for i in range(H):
    arr.append(list(map(int, input().split())))

directy = [1, -1, 0, 0]
directx = [0, 0, 1, -1]

directy2 = [-2, -1, 2, 1, 1, 2, -2, -1]
directx2 = [-1, -2, 1, 2, -2, -1, 1, 2]


used = [[[0] * W for _ in range(H)] for _ in range(K+1)]

# horse_used = [[0] * W for _ in range(H)]


total_result = 21e9
def bfs():
    is_able = 0
    global total_result
    q = deque()
    q.append([0,0,0,0])
    used[0][0][0] = 1
    while q:
        y, x, count, move = q.popleft()
        if y == H-1 and x == W-1:
            is_able = 1
            print(move)

            break
            # print(used[0])
            # print(used[1])

            # return used[K][y][x]
        for i in range(4):
            dy = y + directy[i]
            dx = x + directx[i]
            if not(0 <= dy < H and 0 <= dx < W): continue
            if used[count][dy][dx] != 0: continue
            if arr[dy][dx] == 1: continue
            used[count][dy][dx] = used[count][y][x] + 1
            used[count][dy][dx] = 1
            q.append([dy, dx, count, move+1])

        if count<K:
            for i in range(8):
                dy = y + directy2[i]
                dx = x + directx2[i]
                if not (0 <= dy < H and 0 <= dx < W): continue
                if used[count+1][dy][dx] != 0: continue
                if arr[dy][dx] == 1: continue
                used[count+1][dy][dx] = 1
                # used[count+1][dy][dx] = used[count][y][x] + 1
                q.append([dy, dx, count+1, move + 1])

    if is_able == 0:
        print(-1)
bfs()



# if total_result == 21e9:
#     print(-1)
# else:
#     print(total_result)