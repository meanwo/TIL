import sys

def find_boss(x):
    if arr[x] == -1:
        return x
    else:
        ret = find_boss(arr[x])
        arr[x] = ret
        return ret

def union(a, x, y):
    fx, fy = find_boss(x), find_boss(y)
    if a == 0:
        if fx != fy:
            arr[fy] = fx
        return 1
    else:
        if fx == fy:
            return "YES"
        else:
            return "NO"

# n, m = map(int, input().split())
n, m = map(int, sys.stdin.readline().split())
arr = [-1]*(n+1)
for i in range(m):
    # order, a, b = map(int, input().split())
    order, a, b = map(int, sys.stdin.readline().split())
    if union(order, a, b) != 1:
        print(union(order, a, b))

