import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
result = [0 for _ in range(N+1)]
arr = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])
st, end = map(int, input().split())


heap=[]

def dijkstra(st):
    heapq.heappush(heap,(-int(10e10), st))   # 처음에는 시작점을 경유지로 놓기 (비용 경유지)
    result[st] = int(10e10)                  # 그 다음 부터는 heapq에서 최소 비용을 다음 경유지로 선택

    while heap:
        # print(heap)
        sk, k=heapq.heappop(heap)    # sk=시작점에서 경유지 까지 비용  그리고  k= 경유지
        sk *= -1
        if result[k] > sk: continue   #  result 에서의 업데이트 되어있는 시작점에서->경유지 값 vs
        # 큐에서 방금 뽑은 시작점에서->경유지 값 이랑 비교

        for i in arr[k]:   # 모든 정점에 대해서 (경유지에서 도착할 수 있는 정점을 비교)
            cost = min(sk, i[1])   # cost = 시->경유지 비용 + 경유지에서 도착점까지 최소비용
            if cost > result[i[0]]:
                heapq.heappush(heap,(-cost, i[0]))
                result[i[0]] = cost

dijkstra(st)
print(result[end])
