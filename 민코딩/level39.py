# 1번
# arr = list(map(int, input().split()))
# arr.sort(key = lambda x : -x)
# result = 0
# for i in range(len(arr)):
#     result += arr[i]*i
# print(result)

# 2번
# money_list = [500, 100, 50, 10]
# N = int(input())
# cnt = 0
# for i in range(len(money_list)):
#     cnt += N // money_list[i]
#     N = N % money_list[i]
# print(cnt)

# 3번
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# arr.sort(key=lambda x: x[1])
#
# start_time = arr[0][0]
# end_time = arr[0][1]
# cnt = 1
# for i in range(1, N):
#     if arr[i][0] >= end_time:
#         cnt += 1
#         start_time = arr[i][0]
#         end_time = arr[i][0]
#
# print(cnt)

# 4번
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
# print(arr)
cnt = 0
block = 100
for i in range(N):
    if  block>= arr[i]:
        block -= arr[i]
        cnt+= 1

print(cnt)