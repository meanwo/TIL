import copy
N = list(map(int, input().split()))
#
# # cnt = 0
# def find_total(level, arr, total):
#
#     if level == 3:
#
#         return
#     for i in range(6):
#         backup = N[i]
#         total += N[i]
#         N[i] = 0
#         find_total(level+1, total)
#         N[i] = backup
#
# result = find_total(0,0)
#
# print(result)
# # result = find_total(0, 0)
# # print(result)

def min_total2(arr, min_num):
    used_list = [0]*6
    for i in range(0, 3):
        backup_1 = arr[i]
        # used_list[i] = 1

        # arr[i] = 0
        for j in range(3, 6):
            # if used_list[j] == 0:
            backup_2 = arr[j]
            # used_list[j] = 1
            # arr[j] = 0
            for k in range(1, 5):
                total = 0
                    # if used_list[k] == 0:
                # used_list[k] = 1
                total += arr[i]+arr[j]+arr[k]

                if min_num > total:
                    min_num = total
                    min_used_list = copy.deepcopy(used_list)
                    arr[k] = 0
                arr[j] = 0
        arr[i] = 0
    return min_used_list

result = min_total2(N, 999)
print(result)