def abc(n):
    if n == len(move)-1:
        print(move[n], end=' ')
        return
    print(move[n], end=' ')
    abc(n+1)
    print(move[n], end=' ')




move = list(map(int, input().split()))
abc(0)