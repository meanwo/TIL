
def is_triple(list0):
    arr_dict = {}
    flag = 0
    for i in range(len(list0)):
        if list0[i] not in arr_dict:
            arr_dict[list0[i]] = 1
        elif arr_dict[list0[i]] != 0:
            arr_dict[list0[i]] += 1
    # print(arr_dict)

    for value in arr_dict.values():
        if value >= 3:
            flag = 1
            break
    if flag == 1:
        return 1
    elif flag == 0:
        return 0


def is_run(list0):
    flag = 0
    list0 = list(set(list0))
    list0 = sorted(list0)
    if len(list0) >= 3:
        for i in range(len(list0)-2):
            if list0[i]+2 == list0[i+1]+1 == list0[i+2]:
                flag = 1
                break
    if flag == 1:
        return 1
    else:
        return 0
T = int(input())
for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    print(f'#%d' %test_case, end = ' ')
    # print(arr)

    # print(is_triple([5, 3, 1, 3]))

    list1 = []
    list2 = []
    for i in range(12):
        if i % 2 == 0:
            list1.append(arr[i])
            # print(list1)
            run_1 = is_run(list1)
            triple_1 = is_triple(list1)
            # print(run_1)
            if run_1 == 1 or triple_1 == 1:
                print(1)
                break

        else:
            list2.append(arr[i])
            run_2 = is_run(list2)
            triple_2 = is_triple(list2)
            if run_2 == 1 or triple_2 == 1:
                print(2)
                break

        if i == 11:
            print(0)

