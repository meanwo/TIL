# 1번
# arr = [4, 4, 5, 7, 8, 10, 20, 22, 23, 24]
# def binarySearch(target, left, right):
#     global arr
#     center_index = (left+right)//2
#
#     center_number = arr[center_index]
#     if target == center_number:
#         print('O')
#         # return True
#     elif left == right:
#         print('X')
#     elif center_number > target:
#         binarySearch(target, left, center_index-1)
#     elif center_number < target:
#         binarySearch(target, center_index+1, right)
#
# target = int(input())
# result = binarySearch(target, 0, 9)

# 2번
# arr = list(input())
# def binarySearch(left, right):
#     global arr
#     center_index = (left+right)//2
#     center_signal = arr[center_index]
#     if center_signal == '_' and center_index == 0:
#         print('0%')
#     elif center_signal == '#' and center_index == 9:
#         print('100%')
#     elif center_signal == '#' and arr[center_index+1] == '_':
#         percentage = (center_index+1)*10
#         print(f'%d%%' %percentage)
#     elif center_signal == '_' and arr[center_index+1] == '_':
#         binarySearch(left, center_index-1)
#     elif center_signal == '#' and arr[center_index + 1] == '#':
#         binarySearch(center_index+1, right)
#
# result = binarySearch(0, 9)

# 3번
# M = int(input())
# arr = list(input().split())
# sort_arr = sorted(arr, key=lambda x: x)
# N = int(input())
#
# def binarySearch(target, left, right, cnt, S):
#     global sort_arr
#     center_index = (left+right)//2
#     center = sort_arr[center_index]
#     if target == center:
#         if S >= cnt:
#             # print(cnt)
#             print('pass')
#         else:
#             # print(cnt)
#             print('fail')
#     elif left >= right:
#         print('fail')
#     elif center > target:
#         binarySearch(target, left, center_index-1, cnt+1, S)
#     elif center < target:
#         binarySearch(target, center_index+1, right, cnt+1, S)
#
#
# for i in range(N):
#     title, S = input().split()
#     S = int(S)
#
#     result = binarySearch(title, 0, M-1, 1, S)

# 4번
N = int(input())
arr = [list(input()) for _ in range(N)]
col = [i[0] for i in arr]

def binarySearch(arr, left, right):
    center_index = (left+right)//2
    center_signal = arr[center_index]

    if center_signal == '#' and center_index == 0:
        k = 0
        return k
    elif center_signal == '#' and center_index == N-1:
        k = N-1
        return k
    elif center_signal == '#' and arr[center_index+1] == '0':
        k = center_index
        return k
    elif center_signal == '0' and arr[center_index+1] == '0':
        return binarySearch(arr, left, center_index-1)
    elif center_signal == '#' and arr[center_index + 1] == '#':
        return binarySearch(arr, center_index+1, right)

result = binarySearch(col, 0, N-1)
result2 = binarySearch(arr[result], 0, N-1)

print(result, result2)
