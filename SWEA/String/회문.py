T = int(input())
for i in range(T):
    n, m = list(map(int, input().split()))
    A = [list(input()) for _ in range(n)]
    A_t = [[0]*n for _ in range(n)]

    for j in range(n):
        for k in range(n-m+1):
            for l in range(m):
                if A[j][k+l] == A[j][n-1-l]:
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                circular1 = A[j][k:k+m]
                print(f'#%d' %(i+1), end = ' ')
                print(*circular1, sep ='')

    for j in range(n):
        for k in range(n):
            A_t[k][j] = A[j][k]


    for j in range(n):
        for k in range(n-m+1):
            for l in range(m):
                if A_t[j][k+l] == A_t[j][n-1-l]:
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                circular = A_t[j][k:k+m]
                print(f'#%d' % (i + 1), end=' ')
                print(*circular, sep ='')

