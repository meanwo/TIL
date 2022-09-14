T = int(input())
for test_case in range(1, T+1):

    cnt = 0
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E+1
    leftson = [0]*(V+1)
    rightson = [0]*(V+1)

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if leftson[p] == 0:
            leftson[p] = c
        else:
            rightson[p] = c

    def postorder(n):
        global cnt
        if n:
            postorder(leftson[n])
            postorder(rightson[n])
            cnt +=1

    postorder(N)
    print(f'#%d %d' %(test_case, cnt))