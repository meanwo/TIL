import heapq
#
# arr = []
# heapq.heappush(arr, 4)
# heapq.heappush(arr, 15)
# heapq.heappush(arr, 2)
# heapq.heappush(arr, 7)
# heapq.heappush(arr, 5)
# heapq.heappush(arr, 9)
#
# #log n 속도로 우선순위가 가장 높은 값을 출력
# for i in range(len(arr)):
#     print(heapq.heappop(arr), end=' ')


# arr 배열을 오름차순으로 정렬해보자!
# arr = [4, 87, 4, 24, 8, 23, 3, 7, 4]
# new_arr = []
# for i in range(len(arr)):
#     heapq.heappush(new_arr, arr[i])
# print(new_arr)
#
#
# for i in range(len(new_arr)):
#     print(heapq.heappop(new_arr), end= ' ')

# arr 리스트를 한번에 heap 자료형으로 바꾸기

# arr = [4, 87, 4, 24, 8, 23, 3, 7, 4]

# heapq.heapify(arr)
# # print(arr)
# for i in range(len(arr)):
#     print(heapq.heappop(arr), end= ' ')

# 음수를 곱해서 maxheap 구현
# arr = [4, 87, 4, 24, 8, 23, 3, 7, 4]
# new_list = []
# for i in range(len(arr)):
#     heapq.heappush(new_list, -arr[i])
# # print(new_list)
# for i in range(len(new_list)):
#     print(heapq.heappop(new_list)*-1, end=' ')

# 튜플
# arr = [4, 87, 4, 24, 8, 23, 3, 7, 4]
#
# new_list = []
# for i in range(len(arr)):
#     heapq.heappush(new_list, (-arr[i], arr[i]))
#
# print(new_list)
#
# for i in range(len(new_list)):
#     print(heapq.heappop(new_list)[1], end = '')

# 람다 이용
# vect = [3, 6, 3, 1, 7, 9]
# rev = lambda x:x*-1
# new_list = list(map(rev, vect))
# # 단순 리스트를 heap의 형태로 바꿔줘야함
# heapq.heapify(new_list)
#
# print(new_list)
#
# for i in range(len(new_list)):
#     print(-heapq.heappop(new_list), end= ' ')


# 카드 정렬하기
# N = int(input())
# arr = []
# for i in range(N):
#     arr.append(int(input()))
# heapq.heapify(arr)
# print(arr)
# answer = 0
# while len(arr) > 1:
#     temp1 = heapq.heappop(arr)
#     temp2 = heapq.heappop(arr)
#     answer += (temp1+temp2)
#     heapq.heappush(arr, temp1+temp2)
# print(answer)

# 다익스트라 알고리즘
# 시작점부터 도착점까지 가능 최소비용 구하기
# 시작점에서 도착점까지 바로가는 비용 vs 경유지를 거쳐 도착점까지 가는 비용 중 최소인 것으로 계속 업데이트

# N = 5
# name = 'ABCDE'
# arr = [[0, 3, 999, 9, 5], [999, 0, 7, 999, 1], [999, 999, 0, 1, 999], [999, 999, 999, 0, 999], [999, 999, 1, 999, 0]]
# used = [0] * 5
# result = [0] * 5
#
#
# # A를 시작점으로 간주
# used[0] = 1
# for i in range(N):
#     result[i] = arr[0][i]

# def select_ky():
#     Min = int(21e8)
#     minindex = 0
#     for i in range(N):
#         if used[i] == 0 and result[i] < Min:
#             Min = result[i]
#             minindex = i;
#     return minindex
#
#
# def dijkstra():
#     for i in range(N-1):
#         via = select_ky()  #경유지 선택
#         used[via] = 1
#         for j in range(N):  #모든 정점에 대한 비용을 비교
#             baro = result[j]  #시 -> 도
#             ky = result[via]+arr[via][j]  #경유지를 거친 비용
#             if baro > ky:
#                 result[j] = ky
# dijkstra()
# print(*result)


# 개선된 dijkstra

# 5 정점의 개수
# 7 간선의 개수
# 0 1 3 시작점 도착점 비용
# 0 3 9
# 0 4 5
# 1 2 7
# 1 4 1
# 2 3 1
# 4 2 1
# 0 3   시작점 알고자 하는 도착점 (0번 인덱스에서 3번 인덱스 까지의 최소 비용을 구하겠다.


# 5
# 7
# 0 1 3
# 0 3 9
# 0 4 5
# 1 2 7
# 1 4 1
# 2 3 1
# 4 2 1
# 0 3
# 시작점, 도착점 (0번 인덱스에서 3번 인덱스 까지의 최소 비용을 구하겠다.)

# name='ABCDE'
# n=int(input())
# m=int(input())
# arr=[[] for _ in range(n)]
# for _ in range(m):
#     a,b,c=map(int,input().split())
#     arr[a].append((b,c))
# print(arr)
# start,ed=map(int,input().split())
# inf=int(21e8)
# result=[inf]*n
# heap=[]
#
# def dijkstra(start):
#     heapq.heappush(heap,(0,start))   # 처음에는 시작점을 경유지로 놓기 (비용 경유지)
#     result[start]=0                  # 그 다음 부터는 heapq에서 최소 비용을 다음 경유지로 선택
#
#     while heap:
#         print(heap)
#         sk,k=heapq.heappop(heap)    # sk=시작점에서 경유지 까지 비용  그리고  k= 경유지
#
#         if result[k]<sk: continue   #  result 에서의 업데이트 되어있는 시작점에서->경유지 값 vs
#         # 큐에서 방금 뽑은 시작점에서->경유지 값 이랑 비교
#
#         for i in arr[k]:   # 모든 정점에 대해서 (경유지에서 도착할 수 있는 정점을 비교)
#             cost=sk+i[1]   # cost = 시->경유지 비용 + 경유지에서 도착점까지 최소비용
#             if cost<result[i[0]]:
#                 result[i[0]]=cost
#                 heapq.heappush(heap,(cost,i[0]))
#
# dijkstra(start)
# print(*result)

for i in range(1, -3, -2):
    print(i)