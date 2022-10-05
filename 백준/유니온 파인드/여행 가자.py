import sys

def find_boss(a):
    if boss_list[a] == a:
        return a
    else:
        ret = find_boss(boss_list[a])
        boss_list[a] = ret
        return ret
def union(a, b):
    fa, fb = find_boss(a), find_boss(b)
    if fa == fb:
        return 1
    else:
        boss_list[fb] = fa
        return 0

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
trip_plan = list(map(int, sys.stdin.readline().split()))
boss_list = [i for i in range(N)]

for i in range(N-1):
    for j in range(1, N):
        if arr[i][j] == 1:
            union(i, j)
# print(boss_list)
flag = 1
for i in range(len(trip_plan)-1):
    flag *= union(trip_plan[i]-1, trip_plan[i+1]-1)

if flag == 1:
    print('YES')
else:
    print('NO')



