from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
arr = [0 for _ in range(100001)]
cnt = 0
def bfs(x1):
    global cnt, arr
    q = deque()
    q.append(x1)
    while q:
        x = q.popleft()
        if x == K:
            cnt += 1
        for dx in [x-1, x+1, x*2]:
            if 0 <= dx <= 100000:
                if arr[dx] == 0 or arr[dx] >= arr[x]+1:
                    arr[dx] = arr[x]+1
                    q.append(dx)


if N == K:
    print(0)
    print(1)
else:
    bfs(N)
    print(arr[K])
    print(cnt)

