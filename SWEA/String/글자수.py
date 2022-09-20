T = int(input())

for k in range(T):
    A = [list(input()) for _ in range(2)]
    str_dict = {}
    for i in range(len(A[0])):
        str_dict[A[0][i]] = 0
        for j in range(len(A[1])):
            if A[1][j] == A[0][i]:
                str_dict[A[0][i]] += 1
    print(f'#%d %d' %(k+1, max(str_dict.values())))



