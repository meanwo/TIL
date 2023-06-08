N = int(input())

cnt = 0
col = [0]*N
left_dia = [0]*(2*N-1)
right_dia = [0]*(2*N-1)

def queen(N, i):
    global cnt
    if N == i:
       cnt += 1
    else:
        for j in range(N):
            if check(i, j) == 1:
                col[j] = 1
                left_dia[i+j] = 1
                right_dia[N+i-j-1] = 1
                queen(N, i+1)
                col[j] = 0
                left_dia[i + j] = 0
                right_dia[N + i - j - 1] = 0

def check(i, j):
    if col[j] != 0:
        return 0
    if left_dia[i+j] != 0:
        return 0
    if right_dia[N+i-j-1] != 0:
        return 0
    return 1

queen(N, 0)
print(cnt)
