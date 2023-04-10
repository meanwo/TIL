from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())

dist = [0]*100001
move = [0]*100001


def path(x):
    arr = []
    temp = x
    for _ in range(dist[x]+1):
        arr.append(temp)
        temp = move[temp]
    arr.reverse()
    print(*arr)
def bfs(N):
    global dist, move
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return
        for i in [x-1, x+1, 2*x]:
            if 0 <= i <= 100000:
                if dist[i] == 0:
                    q.append(i)
                    dist[i] = dist[x] + 1
                    move[i] = x

bfs(N)


