T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    arr = sorted(arr, key = lambda x: x[1])
    # print(arr)
    start_time = arr[0][0]
    end_time = arr[0][1]
    cnt = 1
    for i in range(1, N):
        # end_time = arr[i][1]
        if end_time <= arr[i][0]:
            cnt += 1
            start_time = arr[i][0]
            end_time = arr[i][1]
    print(f'#%d %d' %(test_case, cnt))