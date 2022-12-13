# 위상정렬

# arr = [
#     [0,0,0,0,0,0,1],
#     [0,0,1,1,1,0,0],
#     [0,0,0,0,0,1,0],
#     [0,0,0,0,0,1,0],
#     [0,0,0,0,0,0,1],
#     [0,0,0,0,0,0,1],
#     [0,0,0,0,0,0,0],
# ]
# from collections import deque
# N, M = map(int, input().split())
# arr = [[0]*N for _ in range(N)]
# for i in range(M):
#     a, b = map(int, input().split())
#     y = a-1
#     x = b-1
#     arr[y][x] = 1
#
# # print(arr)
# acc=[0]*N
# used=[0]*N
#
# q = deque()
# for j in range(N):          # 사전 작업 개수 등록
#     for i in range(N):
#         if arr[i][j]==1:
#             acc[j]+=1
# print(acc)

# for i in range(N):          # 바로 작업 착수 가능한 것들은
#     if acc[i]==0:           # used에 1체크 하고 q에 등록
#         used[i]=1
#         q.append(i)
#
# while q:
#     now = q.popleft()
#     print(now+1, end = ' ')
#
#     for i in range(N):
#         if arr[now][i]==1 and used[i]==0:
#             if acc[i]==1:
#                 used[i]=1
#                 acc[i]-=1
#                 q.append(i)
#             else:
#                 acc[i]-=1
from collections import deque
N, M = map(int, input().split())
arr = [[] for _ in range(N)]

acc=[0]*N

for i in range(M):
    a, b = map(int, input().split())
    x = a-1
    y = b-1
    arr[x].append(y)
    acc[y] += 1

q = deque()

result = []
for i in range(N):          # 바로 작업 착수 가능한 것들은
    if acc[i]==0:           #  q에 등록
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)

    for i in arr[now]:
        if acc[i]==1:
            acc[i]-=1
            q.append(i)
        else:
            acc[i]-=1

for i in result:
    print(i+1, end = ' ')