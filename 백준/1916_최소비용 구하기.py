import heapq
N = int(input())
M = int(input())

arr = [[] for _ in range(N+1)]
result = [int(21e9) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
st, ed = map(int, input().split())

heap = []
def min_cost(st, ed):
    heapq.heappush(heap, (0, st))
    result[st] = 0
    while heap:
        cost1, k = heapq.heappop(heap)
        if result[k] < cost1: continue
        for i in arr[k]:
            cost2 = i[1] + cost1
            if cost2 < result[i[0]]:
                result[i[0]] = cost2
                heapq.heappush(heap, (cost2, i[0]))
    return result[ed]

print(min_cost(st, ed))
