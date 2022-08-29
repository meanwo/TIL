
for i in range(10):
    test_num = int(input())
    A = [list(input()) for _ in range(100)]
    A_t = [[0]*100 for _ in range(100)]
    max_cnt = 0

    for j in range(100):
        for k in range(100, 1, -1):
            for l in range(100-k+1):
                for m in range(k//2):
                    if A[j][l+m] == A[j][k-1+l-m]:
                        flag = 1
                    else:
                        flag = 0
                        break
                if flag == 1:
                    break
            if flag == 1:
                if k > max_cnt:
                    max_cnt = k
                    break


    for j in range(100):
        for k in range(100):
            A_t[k][j] = A[j][k]


    for j in range(100):
        for k in range(100, 0, -1):
            for l in range(100-k+1):
                for m in range(k//2):
                    if A_t[j][l+m] == A_t[j][k-1+l-m]:
                        flag = 1
                    else:
                        flag = 0
                        break
                if flag == 1:
                    break
            if flag == 1:
                if k > max_cnt:
                    max_cnt = k
                    break
    print(f'#%d %d' %(test_num, max_cnt))
