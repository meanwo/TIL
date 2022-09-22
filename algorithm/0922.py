# # atm 최소 대기시간 문제(내 풀이)
# N = int(input())
# arr = list(map(int, input().split()))
# sum = 0
# total_sum = 0
# def least_time(N, arr):
#     global sum, total_sum
#     for i in range(N):
#         min_arr = min(arr)
#         sum += min_arr
#         arr[arr.index(min_arr)] = 999
#         total_sum += sum
#     return total_sum
#
# result = least_time(N, arr)
# print(result)
# # atm 최소 대기시간 문제
# n=int(input())
# time_w=list(map(int,input().split()))
#
# time_w.sort(reverse=True)
#
# answer=0
# for i in range(1,n+1):
#     answer+=(i*time_w[i-1])
#
# print(answer)


# 파티룸 예약 문제
# 10
# 18 21
# 11 14
# 15 17
# 18 22
# 13 16
# 10 16
# 12 23
# 22 24
# 16 20
# 15 19

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range (N)]
# arr.sort(key = lambda x : x[1])
# print(arr)
# cnt = 0
# before_time = -1
#
# for i in range(N):
#     if before_time <= arr[i][0]:
#         before_time = arr[i][1]
#         cnt += 1
# print(cnt)


# bottom-up 방식으로 유류비가 최소가 되도록 만들기

# arr = [
#     [0,1,1,9],
#     [4,2,2,3],
#     [1,3,4,1],
#     [3,7,8,0]
# ]
#
# arr1 = [[0]*4 for _ in range(4)]
#
# for i in range(1,4):
#     arr1[0][i] = arr1[0][i-1]+arr[0][i]
#     arr1[i][0] = arr1[i-1][0]+arr[i][0]
#
# for i in range(1,len(arr)):
#     for j in range(1,len(arr)):
#         arr1[i][j] = min(arr1[i-1][j],arr1[i][j-1]) + arr[i][j]


# knapsack, flexional 냅색도 참고하기!
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12

# N, K = map(int, input().split())
# w_v_list = []
# for i in range(N):
#     W, V = map(int, input().split())
#     w_v_list.append([W, V])
#
# print(w_v_list)
# arr = [[0]*(K+1) for _ in range(N+1)]
#
#
# for i in range(1, N+1):
#     for j in range(1, K+1):
#         if j >= w_v_list[i-1][0]:
#             arr[i][j] = w_v_list[i-1][1]+arr[i-1][j-w_v_list[i-1][0]]
#
# max_value = 0
# for i in range(N+1):
#     for j in range(K+1):
#         if arr[i][j] > max_value:
#             max_value = arr[i][j]
# # print(arr)
# print(max_value)

# 냅색 다른 풀이
# n, k = map(int, input().split())
# knapsack = [[0 for _ in range(k + 1)] for _ in range(n + 1)]  # 배열
#
# item = [[0, 0]]
# for i in range(1, n + 1):  # 아이템 입력
#     item.append(list(map(int, input().split())))
#
# for i in range(1, n + 1):  # 아이템 개수만큼 반복
#     for j in range(1, k + 1):  # 최대무게까지 반복
#
#         weight = item[i][0]
#         value = item[i][1]
#
#         if j < weight:  # 가방에 넣을 수 없으면
#             knapsack[i][j] = knapsack[i - 1][j]  # 위에 값 그대로 가져오기
#         else: # 가방에 넣을 수 있으면
#             knapsack[i][j] = max(knapsack[i - 1][j],value + knapsack[i][j - weight])
#             # 위에 값 vs
#             # 현재 아이템 가치 + 그전 단계에서 구한 남은무게의 가치
#
# print(knapsack[n][k])

# 동전교환
# coin=[1,7,10]
# n=int(input())
# arr = [[0 for _ in range(n+1)] for _ in range(3)]  # 배열
# for i in range(3):
#     for j in range(n+1):
#         mok=j//coin[i]
#         if j%coin[i]==0: arr[i][j]=mok
#         else:
#             if mok==0: arr[i][j]=arr[i-1][j]
#             else:
#                 arr[i][j]=min(arr[i-1][j],mok+arr[i][j%coin[i]])
# print(arr[2][n])


