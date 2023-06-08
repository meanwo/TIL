import heapq
N, M, X = map(int, input().split())
arr = [[] for _ in range(N+1)]
result = [int(21e9) for _ in range(N+1)]
for _ in range(M):
    st, ed, time = map(int, input().split())
    arr[st].append([ed, time])



heap = []
def party(st):
    result = [int(21e9) for _ in range(N + 1)]
    heapq.heappush(heap, (0, st))
    result[st] = 0
    while heap:
        cost1, k = heapq.heappop(heap)
        if result[k] < cost1: continue

        for i in arr[k]:
            cost2 = cost1 + i[1]
            if cost2 < result[i[0]]:
                heapq.heappush(heap, (cost2, i[0]))
                result[i[0]] = cost2
    return result

first_distance = []
for i in range(N):
    first_distance.append(party(i+1)[X])
# print(first_distance)

second_distance = party(X)[1:]
# print(second_distance)

total_distance = [x+y for x, y in zip(first_distance, second_distance)]
print(max(total_distance))

