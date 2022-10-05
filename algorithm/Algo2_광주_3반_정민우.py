def dfs(jam_list, idx, arr, total):
    global gap, best_total
    if total > M:
        return

    if idx == len(arr):
        if 0 <= (M - total) and (M-total) < gap:
            gap = M - total
            best_total = total
        return


    else:
        # 원하는 보석일 때는 그것을 포함할지, 하지 않을지 두가지 경우로 나뉘어짐
        jam_list.append(arr[idx])
        dfs(jam_list, idx+1, arr, total+arr[idx])
        jam_list.pop()
        dfs(jam_list, idx+1, arr, total)
T = int(input())
for test_case in range(1, T+1):

    N, M = map(int, input().split())
    arr_base = list(map(int, input().split()))
    arr = []
    wanted_jam = [4, 6, 7, 9, 11]
    jam_list = []
    gap = 9999
    best_total = 0
    # 원하는 보석만 걸러내는 과정
    for i in range(len(arr_base)):
        for j in range(len(wanted_jam)):
            if arr_base[i] % wanted_jam[j] == 0:
                arr.append(arr_base[i])
                break

    dfs([], 0, arr, 0)
    print(f'#%d %d' %(test_case, best_total))