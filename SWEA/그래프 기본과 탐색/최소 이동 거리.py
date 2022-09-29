import heapq
def dijkstra(start):
    heapq.heappush(new_list, (0, start))
    result[start] = 0
    while new_list:
        sk, k = heapq.heappop(new_list)

        if result[k] < sk: continue

        for i in arr[k]:
            cost = sk+i[1]
            if cost<result[i[0]]:
                result[i[0]] = cost
                heapq.heappush(new_list,(cost, i[0]))
T = int(input())
for test_case in range(1, T+1):
    N, E = map(int, input().split())
    # print(N, E)
    arr = [[] for _ in range(N+1)]

    for _ in range(E):
        a, b, c = map(int, input().split())
        arr[a].append((b,c))

    inf = int(21e8)
    result = [inf]*(N+1)

    new_list = []


    dijkstra(0)
    print(f'#%d %d' %(test_case, result[N]))

