N = int(input())
y1, x1, y2, x2 = map(int, input().split())
virus = [(y1, x1, 1), (y2, x2, 1)]
arr = [[0]*N for _ in range(N)]
directx = [-1, 1, 0, 0]
directy = [0, 0, 1, -1]

def bfs(virus):


    while virus:
        y, x, level = virus.pop(0)
        arr[y][x] = level

        for i in range(4):
            dy = y+directy[i]
            dx = x+directx[i]
            if not (0<= dy <N and 0<= dx < N): continue
            if arr[dy][dx] != 0: continue
            arr[dy][dx] = arr[y][x]+1
            virus.append((dy, dx, level+1))

bfs(virus)

for i in range(N):
    print(*arr[i], sep='')