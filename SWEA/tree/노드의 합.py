T = int(input())

for test_case in range(1, T+1):

    N, M, L = map(int, input().split())
    N_list = [0] * (N+1)

    for i in range(M):
        a, b = map(int, input().split())
        N_list[a] = b

    def postorder(now):
        global N_list
        if now > N:
            return
        postorder(now*2)
        postorder(now*2+1)
        if now*2+1 <= N:
            N_list[now] = N_list[now*2]+N_list[now*2+1]
        elif now*2+1 > N and now*2 <=N:
            N_list[now] = N_list[now*2]

    result = postorder(1)

    print(f'#%d %d' %(test_case, N_list[L]))