def bfs(S, G):
    queue = [S]
    visited[S] = 1

    while queue:
        node = queue.pop(0)
        if node == G:
            return distance[node]
        for j in range(V):
            if arr[node][j] == 1:
                if visited[j] == 0:
                    visited[j] = 1
                    distance[j] = distance[node] + 1
                    queue.append(j)
    return 0
T = int(input())
for i in range(T):
    V, E = map(int, input().split())
    arr = [[0]*V for _ in range(V)]
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a-1][b-1] = 1
        arr[b-1][a-1] = 1
    S, G = map(int, input().split())
    S -= 1
    G -= 1
    visited = [0]*V
    distance = [0]*V
    result = bfs(S,G)
    print(f'#%d %d' %(i+1, result))

