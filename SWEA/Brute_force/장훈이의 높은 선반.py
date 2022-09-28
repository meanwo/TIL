

T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    height.sort(reverse=True)
    total = 0
    for i in range(N):
        total += height[i]

        if total == B:
            print(f'#%d %d' % (test_case, 0))
        elif total > B:


    print(f'#%d %d' %(test_case, min_dif))