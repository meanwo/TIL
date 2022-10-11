import copy


def find_max(total, y1, x1, idx, honey):
    global max_total

    if idx == M or honey < arr[y1][x1]:
        if max_total < total:
            max_total = total
        return
    else:
        backup_honey = honey
        backup_total = copy.deepcopy(total)
        honey -= arr[y1][x1]
        total += arr[y1][x1]**2
        find_max(total, y1, x1+1, idx+1, honey)
        honey = backup_honey
        total = backup_total
        find_max(total, y1, x1+1, idx+1, honey)
        # honey += arr[y1][x1]
        # total -= arr[y1][x1] ** 2

N, M, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# max_result = 0
square_arr = [[0]*(N-M+1) for _ in range(N)]
# part_used = [[0]*M]
# used = [[0]*(N-M+1) for _ in range(N)]
for i in range(N):
    for j in range(N-M+1):
        total = 0
        max_total = 0
        find_max(0, i, j, 0, C)
        square_arr[i][j] = max_total

print(square_arr)

# max_total = 0
# find_max(0, 0, 1, 0, C)
# print(max_total)

# 4 3 12
# 8 8 6 5
# 5 2 7 4
# 8 5 1 7
# 7 8 9 4

# 3 2 10
# 1 3 9
# 2 4 9
# 3 3 9
