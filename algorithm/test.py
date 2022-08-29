n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]

idx = [5, 3, 4, 1, 2, 0]

# sum_max = 0
# def dice(level, floor):
#     global sum_max
#
#     if level == n:
#         return sum_max
#     if arr[level].index(floor) == 5 or arr[level].index(floor) == 0:
#         sum_max += max(arr[level][1:5])
#     elif arr[level].index(floor) == 4 or arr[level].index(floor) == 2:
#         sum_max += max(arr[level][0], arr[level][1], arr[level][3], arr[level][5])
#     elif arr[level].index(floor) == 1 or arr[level].index(floor) == 3:
#         sum_max += max(arr[level][0], arr[level][2], arr[level][4], arr[level][5])
#
#     floor = arr[level][idx[arr[level].index(floor)]]
#     return dice(level+1, floor)

result_max = 0
for i in range(6):
    floor = arr[0][i]
    sum_max = 0
    for level in range(n):
        if arr[level].index(floor) == 5 or arr[level].index(floor) == 0:
            sum_max += max(arr[level][1:5])
        elif arr[level].index(floor) == 4 or arr[level].index(floor) == 2:
            sum_max += max(arr[level][0], arr[level][1], arr[level][3], arr[level][5])
        elif arr[level].index(floor) == 1 or arr[level].index(floor) == 3:
            sum_max += max(arr[level][0], arr[level][2], arr[level][4], arr[level][5])

        floor = arr[level][idx[arr[level].index(floor)]]

    if sum_max > result_max:
        result_max = sum_max

    # result = dice(0, arr[0][i])
    # if sum_max > result_max:
    #     result_max = sum_max


print(result_max)