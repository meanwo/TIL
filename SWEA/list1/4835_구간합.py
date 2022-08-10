T = int(input())
for i in range(T):
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))

    # 초깃값 설정
    max_sum = 0
    min_sum = 0
    for j in range(M):
        max_sum += A[j]
        min_sum += A[j]

    for j in range(N-M+1):
        sum_N = 0
        for k in range(j, M+j):
            sum_N += A[k]
        if max_sum < sum_N:
            max_sum = sum_N
        if min_sum > sum_N:
            min_sum = sum_N

    print(f'#%d %d' %(i+1, max_sum-min_sum))