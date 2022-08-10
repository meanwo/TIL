for i in range(10):
    n = int(input())
    box = list(map(int, input().split()))
    bucket = [0]*101
    for j in range(len(box)):
        bucket[box[j]] += 1
    while n:
        if bucket[0] != 0 and bucket[-1] != 0:
            bucket[0] -= 1
            bucket[1] += 1
            bucket[-1] -= 1
            bucket[-2] += 1
            n -= 1

        if bucket[0] == 0:
            bucket = bucket[1:]
        if bucket[-1] == 0:
            bucket = bucket[0:-1]
    print(f'#%d %d' %(i+1, len(bucket)-1))
