import copy
T = int(input())

for test_case in range(1, T+1):

# 1 1 7 1
# 2 1 7 1
# 5 1 5 4
# 3 2 8 4
# 4 3 14 1
# 3 4 3 3
# 1 5 8 2
# 3 5 100 1
# 5 5 1 1


# 7 5 724 2
# 7 7 464 3
# 2 2 827 2
# 2 4 942 4
# 4 5 604 4
# 7 2 382 1
# 6 5 895 3
# 8 7 538 4
# 6 1 299 4
# 4 7 811 4
# 3 6 664 2
# 6 8 868 2
# 7 6 859 2
# 4 6 778 2
# 5 4 842 3
# 1 3 942 1
# 1 1 805 3
# 3 2 350 3
# 2 5 623 2
# 5 3 840 1
# 7 1 308 4
# 1 8 323 3
# 2 3 82 3
# 2 6 115 2
# 8 3 930 1
# 6 2 72 1
# 2 1 290 3
# 4 8 574 4
# 8 5 150 3
# 8 2 287 2
# 2 8 909 2
# 2 7 588 2
# 7 3 30 3
# 5 8 655 3
# 3 8 537 1
# 4 2 350 3
# 5 6 199 1
# 5 5 734 2
# 3 3 788 1
# 8 4 893 1
# 1 4 421 4
# 6 3 616 2
# 1 2 556 4
# 7 8 8 1
# 5 2 702 2
# 4 4 503 3
    directx = [0, 0, -1, 1]
    directy = [-1, 1, 0, 0]
    N, M, K = map(int, input().split())
    arr = [[[0, 0]]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == 0 or i == N-1:
                arr[i][j] = 'x'
            elif j == 0 or j == N-1:
                arr[i][j] = 'x'
    # next_arr = copy.deepcopy(arr)
    next_arr = [[[0, 0]]*N for _ in range(N)]

    for i in range(K):
        y, x, count, dir = map(int, input().split())
        arr[y][x] = [count, dir]

    # print(arr)
    for i in range(M):
        next_arr = [[[0, 0]]*N for _ in range(N)]

        for j in range(N):
            for k in range(N):
                # 위쪽 방향
                if arr[j][k] != 'x' and arr[j][k][1] == 1 and next_arr[j-1][k] == [0, 0]:
                    if j == 1:
                        next_arr[j-1][k] = [arr[j][k][0]//2, 2]
                    else:
                        next_arr[j-1][k] = arr[j][k]
                elif arr[j][k] != 'x' and arr[j][k][1] == 1 and next_arr[j-1][k] != [0,0]:
                    next_arr[j-1][k][1] = max(arr[j][k], next_arr[j-1][k])[1]
                    next_arr[j-1][k][0] += arr[j][k][0]

                # 아래쪽 방향
                if arr[j][k] != 'x' and arr[j][k][1] == 2 and next_arr[j+1][k] == [0,0]:
                    if j == N-2:
                        next_arr[j+1][k] = [arr[j][k][0]//2, 1]
                    else:
                        next_arr[j+1][k] = arr[j][k]
                elif arr[j][k] != 'x' and arr[j][k][1] == 2 and next_arr[j+1][k] != [0,0]:
                    next_arr[j+1][k][1] = max(arr[j][k], next_arr[j+1][k])[1]
                    next_arr[j+1][k][0] += arr[j][k][0]

                # 왼쪽 방향
                if arr[j][k] != 'x' and arr[j][k][1] == 3 and next_arr[j][k-1] == [0,0]:
                    if k == 1:
                        next_arr[j][k-1] = [arr[j][k][0]//2, 4]
                    else:
                        next_arr[j][k-1] = arr[j][k]
                elif arr[j][k] != 'x' and arr[j][k][1] == 3 and next_arr[j][k-1] != [0,0]:
                    next_arr[j][k-1][1] = max(arr[j][k], next_arr[j][k-1])[1]
                    next_arr[j][k-1][0] += arr[j][k][0]

                # 오른쪽 방향
                if arr[j][k] != 'x' and arr[j][k][1] == 4 and next_arr[j][k+1] == [0,0]:
                    if k == N-2:
                        next_arr[j][k+1] = [arr[j][k][0]//2, 3]
                    else:
                        next_arr[j][k+1] = arr[j][k]
                elif arr[j][k] != 'x' and arr[j][k][1] == 4 and next_arr[j][k+1] != [0,0]:
                    next_arr[j][k+1][1] = max(arr[j][k], next_arr[j][k+1])[1]
                    next_arr[j][k+1][0] += arr[j][k][0]
        # print(next_arr)
        for j in range(N):
            for k in range(N):
                arr[j][k] = next_arr[j][k]

    # print(arr)
    total = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j][0] != 0:
                total+= arr[i][j][0]
    print(f'#%d %d' %(test_case, total))

# a = [8,4]
# b = [3,3]
# b[1] = max(a, b)[1]
#
# b[0] += a[0]
# print(b)

