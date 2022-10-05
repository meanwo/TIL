def queen(i, N):
    global cnt
    if i == N:
        cnt += 1
    else:
        for j in range(N):
            if check(i, j) == 1:
                col[j] = 1
                left_dia[i+j] = 1
                right_dia[N + i - j - 1] = 1
                queen(i+1, N)
                col[j] = 0
                left_dia[i+j] = 0
                right_dia[N + i - j - 1] = 0

def check(i, j):
    if col[j] == 1:
        return 0
    if left_dia[i+j] == 1:
        return 0
    if right_dia[N+i-j-1] == 1:
        return 0
    return 1

T = int(input())
for test_case in range(1, T+1):
    N= int(input())
    visit = [[0]*N for _ in range(N)]
    col = [0]*N
    left_dia = [0]*(2*N-1)
    right_dia = [0]*(2*N-1)


    cnt = 0
    queen(0, N)
    print(f'#%d %d' %(test_case, cnt))
