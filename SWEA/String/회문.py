T = int(input())
for i in range(T):
    n, m = list(map(int, input().split()))
    A = [list(input()) for _ in range(n)]
    A_t = [[0]*n for _ in range(n)]
    # print(A)
    # circular1 = 0
    # circular2 = 0
    for j in range(n):
        for k in range(n-m+1):
            for l in range(m):
                if A[j][k+l] == A[j][m-1-k-l]:
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                circular1 = A[j][k:k+m]
                print(*circular1, sep ='')

    for j in range(n):
        for k in range(n):
            A_t[k][j] = A[j][k]
    print(A_t)

    for j in range(n):
        for k in range(n-m+1):
            for l in range(m):
                if A_t[j][k+l] == A_t[j][m-1-k-l]:
                    flag = 1
                else:
                    flag = 0
                    break
            if flag == 1:
                circular = A_t[j][k:k+m]
                print(*circular, sep ='')



        #     if A[k][j] == A[n-1-k][j]:
        #         flag = 1
        #     else:
        #         flag = 0
        #         break
        # if flag == 1:
        #     circular2 = A[j][k]
        #     print(*circular2, sep ='')
