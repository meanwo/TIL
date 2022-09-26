T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))

    N_list.sort(key= lambda x: -x)
    M_list.sort(key= lambda x: -x)
    # print(M_list)
    # print(N_list)

    total = 0
    idx1 = 0
    idx2 = 0
    while True:
        if idx2 >= N or idx1 >= M:
            break
        if M_list[idx1] < N_list[idx2]:
            idx2 += 1
        elif M_list[idx1] >= N_list[idx2]:
            total += N_list[idx2]
            idx1 += 1
            idx2 += 1
    print(f'#%d %d' %(test_case, total))