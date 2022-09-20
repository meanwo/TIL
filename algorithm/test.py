import copy
# N = list(map(int, input().split()))
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

# result = min_total2(N, 999)
# print(result)
arr = list(map(int, input().split()))


# def find_total(level, arr, total):
#     if level == 3:
#         print(total, arr)
#         return
#     if level == 0:
#         for i in range(0, 3):
#             backup_sum1 = total
#             total += arr[i]
#             backup1 = arr[i]
#             arr[i] = 0
#             # print(arr, total)
#             find_total(level+1, arr, total)
#             arr[i] = backup1
#             total = backup_sum1
#     if level == 1:
#         for i in range(3, 6):
#             backup_sum2 = total
#             total += arr[i]
#             backup2 = arr[i]
#             arr[i] = 0
#             # print(arr, total)
#             find_total(level+1, arr, total)
#             arr[i] = backup2
#             total = backup_sum2
#     if level == 2:
#         for i in range(1, 5):
#             backup_sum3 = total
#             total += arr[i]
#             backup3 = arr[i]
#             arr[i] = 0
#             # print(arr, total)
#             find_total(level+1, arr, total)
#             arr[i] = backup3
#             total = backup_sum3
#
# turn_result = find_total(0, arr, 0)
#
# print(turn_result)
def min_except_zero(arr, min_num):
    for i in range(len(arr)):
        if arr[i] != 0 and min_num > arr[i]:
            min_num = arr[i]
    return min_num


def find_total(level, arr, total):
    if level == 3:
        print(total, arr)
        return

    for i in range(len(arr)):
        zero_cnt = 0
        if arr[i] == 0:
            zero_cnt += 1

        if zero_cnt < 3:
            min_num = min_except_zero(arr, 999)
            total += min_num
            arr[arr.index(min_num)] = 0

        elif zero_cnt >= 3:




