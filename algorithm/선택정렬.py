def selectionSort(a, N):
    for i in range(N-1):   # N개의 배열이 있다면 마지막 비교는 N-2와 N-1 번째 요소.
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j
            a[i], a[minIdx] = a[minIdx], a[i]

