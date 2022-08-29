T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    # print(N, M)
    num = list(map(int, input().split()))
    for j in range(M):
        num.append(num.pop(0))
    print(f'#%d %d' %(i+1,num[0]))
