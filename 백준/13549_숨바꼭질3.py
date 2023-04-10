from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
arr = [0 for _ in range(100001)]

def bfs(x1):
    global arr
    q = deque()
    q.append([x1, 0])
    while q:
        x, cnt = q.popleft()

        if x == K:
            return cnt
        for i in range(3):
            if i == 0:
                dx = x*2
                temp_cnt = cnt
            elif i == 1:
                dx = x-1
                temp_cnt = cnt + 1
            else:
                dx = x+1
                temp_cnt = cnt + 1

            if 0 <= dx <= 100000:
                if arr[dx] == 0:
                    arr[dx] = 1
                    q.append([dx, temp_cnt])


result = bfs(N)
print(result)