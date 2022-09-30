# 최장공통부분 문자열
# word1 = input()
# word2 = input()
#
# arr = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]
#
# for i in range(len(word1)):
#     for j in range(len(word2)):
#         if word1[i] == word2[j]:
#             arr[i+1][j+1] = arr[i][j]+1
# print(arr)

# 최장공통부분 수열
# word1 = input()
# word2 = input()
#
# arr = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]
#
# for i in range(len(word1)):
#     for j in range(len(word2)):
#         if word1[i] == word2[j]:
#             arr[i+1][j+1] = arr[i][j]+1
#         else:
#             arr[i+1][j+1] = max(arr[i][j+1], arr[i+1][j])
# print(arr)


# # 최장 증가 부분 수열
# N = int(input())
# arr = list(map(int, input().split()))
# result = [1]*N
#
# for i in range(1, N):
#     part_result = 1
#     factor_list = []
#     for j in range(i):
#         if arr[i] > arr[j] and arr[j] not in factor_list:
#             factor_list.append(arr[j])
#             part_result += 1
#     if part_result > result[i]:
#         result[i] = part_result
#
# print(result)


# floyd warshall algorithm
#  모든 정점에서 모든 정점으로의 최단경로
# (dijkstra-시작점(한 정점)에서 모든 정점까지의 최단 경로)
# inf=(int)(21e8)
# arr=[
#     [0,5,inf,8],
#     [7,0,9,inf],
#     [2,inf,0,4],
#     [inf,inf,3,0]
# ]
# for k in range(4):
#     for s in range(4):
#         for d in range(4):
#             if arr[s][d]>arr[s][k]+arr[k][d]:
#                 arr[s][d]=arr[s][k]+arr[k][d]
#
# for i in range(4):
#     for j in range(4):
#         print(arr[i][j],end=' ')
#     print()


def dfs(now):
    global result
    if now == end:
        return 1

    for j in range(len(arr[now])):
        if len(arr[now]) == 0: continue
        dfs(arr[now][j])
T=int(input())

for tc in range(1,1+T):
    v,e = map(int,input().split())
    arr = [[] for _ in range(v + 1)]
    for _ in range(e):
        st, ed = map(int,input().split())
        arr[st].append(ed)
    start,end= map(int,input().split())
    # print(arr)
    result=0


    dfs(start)
    # print(result)
    print(f'#{tc} {result}')
