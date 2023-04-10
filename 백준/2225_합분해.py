N, K = map(int, input().split())
arr = [[0]*(N+1) for _ in range(K+1)]
for i in range(2):
    for j in range(N+1):
        arr[i][j] = 1

# print(arr)
# 3번 더해 2 만들기
# => 2를 2개로 만들기 + 1을 2개로 만들기 + 0을 2개로 만들기

for i in range(2, K+1):
    for j in range(N+1):
        for k in range(j+1):
            arr[i][j] += arr[i-1][k]

print(arr[-1][-1]%1000000000)
# def dp(K, N):
#     global result
#     if K == 1:
#         result += 1
#         return
#     elif K == 2:
#         result += N+1
#         return
#     else:
#         for i in range(N+1):
#             dp(K-1, i)
#
# dp(K,N)
# print(result % 1000000000)


