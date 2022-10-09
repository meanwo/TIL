N, M, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
used = [[0]*N for _ in range(N)]

print(arr)

def dfs(y1, x1):
    for i in range(N):
        for j in range(N-M+1):
            if used[i][j] == 1: continue
