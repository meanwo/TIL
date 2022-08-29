T = int(input())
for test_case in range(T):
    arr = [list(map(int, input().split())) for _ in range(9)]
    flag = 1
    for j in range(9):
        num_list = [i for i in range(1, 10)]
        num_list2 = [i for i in range(1, 10)]
        for k in range(9):
            if arr[j][k] not in num_list:
                flag = 0
                break
            if arr[k][j] not in num_list2:
                flag = 0
                break
            num_list.remove(arr[j][k])
            num_list2.remove(arr[k][j])
        if flag == 0:
            break
    for j in range(3):
        for k in range(3):
            num_list_3 = [i for i in range(1, 10)]
            for l in range(3):
                for m in range(3):
                    if arr[l+3*j][m+3*k] not in num_list_3:
                        flag = 0
                        break
                    num_list_3.remove(arr[l+3*j][m+3*k])
                if flag == 0:
                    break
            if flag == 0:
                break
        if flag == 0:
            break

    print(f'#%d %d' %(test_case+1, flag))
