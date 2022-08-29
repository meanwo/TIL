T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus_stop = []
    cnt_list = [0]*P
    for i in range(P):
        bus_stop.append(int(input()))

    for i in range(P):
        for k in range(N):
            if arr[k][0] <= bus_stop[i] <= arr[k][1]:
                cnt_list[i] += 1
    print(f'#%d' %(test_case), end= ' ')
    print(*cnt_list, sep = ' ')