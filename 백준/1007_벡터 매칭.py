import sys
from itertools import combinations
import copy
import math
T = int(sys.stdin.readline())

for test_case in range(T):
    N = int(sys.stdin.readline())
    arr = []
    x_total = 0
    y_total = 0
    for i in range(N):
        x, y = map(int, sys.stdin.readline().split())
        x_total += x
        y_total += y
        arr.append([x, y])

    comb = list(combinations(arr, N//2))
    distance = 21e9
    # print(comb[0][0], comb[0][1], comb[1][0], comb[1][1])
    for i in range(len(comb)):
        x_temp = copy.deepcopy(x_total)
        y_temp = copy.deepcopy(y_total)
        for j in range(N//2):
            # 모든 점의 x좌표 합에서 시점(혹은 종점)x좌표 값을 두번 빼야 벡터의 합의 x좌표
            x_temp -= 2*comb[i][j][0]
            y_temp -= 2*comb[i][j][1]
        distance = min(distance, math.sqrt((x_temp*x_temp+y_temp*y_temp)))
    print(distance)


