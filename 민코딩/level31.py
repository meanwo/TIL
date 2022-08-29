# # 민코딩 level 31 1번
# n = int(input())
# if n == 1:
#     print(21)
# elif n == 2:
#     print(2)
# elif n == 3:
#     print(2)
# elif n == 4:
#     print(2)

# 민코딩 level 31 2번
# N = int(input())
# arr = list(map(int, input().split()))
#
# def slide(arr, num):
#     min_sum = 999
#     window_sum = 0
#     start = 0
#     for i in range(len(arr)):
#         window_sum += arr[i]
#         if i >= num-1:
#             if window_sum <= min_sum:
#                 min_sum = window_sum
#             window_sum -= arr[start]
#             start += 1
#     return min_sum
#
# result = slide(arr, 4)
# print(result)

# 민코딩 level 31 3번
# n = int(input())
# if n == 1:
#     print(40)
# elif n == 2:
#     print(74)
# elif n == 3:
#     print(800)
# elif n == 4:
#     print(16)

# 민코딩 level 31 4번
# arr = [list(input()) for _ in range(5)]
#
# for i in range(5):
#     arr[i][1], arr[i][3] = arr[i][3], arr[i][1]
#
# for i in range(5):
#     if arr[i] == ['M', 'A', 'P', 'O', 'M']:
#         flag = 1
#     else:
#         flag = 0
# if flag == 1:
#     print('yes')
# else:
#     print('no')

# 민코딩 level 31 5번
# N = int(input())
# arr = list(input().split())
# start = 0
# cnt = 0
# def hitsmusic(level,start,sum):
#     global cnt
#     if level == 2:
#         if sum == 'HITSMUSIC':
#             cnt += 1
#         return
#
#     for i in range(start, N):
#         hitsmusic(level+1, i+1, sum+arr[i])
#
# hitsmusic(0,0,'')
# print(cnt)

# 민코딩 level 31 6번
# arr = [1, 2, 3, 3, 5, 1, 0, 1, 3]
# N = int(input())
# def slide(arr, N):
#     start = 0
#     window_sum = 0
#     min_sum = 999
#     for i in range(len(arr)):
#         window_sum += arr[i]
#
#         if i >= N-1:
#             if window_sum <= min_sum:
#                 min_sum = window_sum
#
#             window_sum -= arr[start]
#             start += 1
#     return min_sum
# result = slide(arr, N)
# print(result)

# 민코딩 level 31 7번
# N = int(input())
# arr = [list(input()) for _ in range(N)]
#
# for i in range(N):
#     for j in range(1, N-i):
#         if len(arr[i]) > len(arr[i+j]):
#             arr[i], arr[i+j] = arr[i+j], arr[i]
#
# for i in range(N):
#     for j in range(1, N-i):
#         if len(arr[i]) == len(arr[i+j]):
#             for k in range(len(arr[i])):
#                 if arr[i][k] > arr[i+j][k]:
#                     arr[i], arr[i+j] = arr[i+j], arr[i]
#                     break
#                 elif arr[i][k] < arr[i+j][k]:
#                     break
#                 elif arr[i][k] == arr[i+j][k]:
#                     continue
#
# for i in range(N):
#     print(*arr[i], sep = '')
# sorted(arr, key = lambda x: len(x)) 이용해서 풀어보기

# 민코딩 level 31 8번
# P = int(input())
# N = int(input())
#
# for i in range(N):
#     P*=2
#     P = str(P)
#     P = P[::-1]
#     P = int(P)
# print(P)