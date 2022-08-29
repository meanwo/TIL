M = int(input())
arr = list(map(int, input().split()))
n = int(input())


def switch(num):
    if num == 1:
        num = 0
    elif num == 0:
        num = 1
    return num

for i in range(n):
    a, b = map(int, input().split())
    if a == 1:
        for j in range(M):
            if (j+1)%b == 0:
                arr[j] = switch(arr[j])

    elif a == 2:
        for j in range(M):
            if 0 <= b-1-j and b-1+j < M and arr[b-1-j] == arr[b-1+j]:
                arr[b-1-j] = switch(arr[b-1-j])
                if j != 0:
                    arr[b - 1 + j] = switch(arr[b - 1 + j])
            elif 0 > b-1-j or b-1+j >= M or arr[b-1-j] != arr[b-1+j]:
                break

for i in range(len(arr)):
    for j in range(20):
        if len(arr)-1 >= 20*i+j:
            print(arr[20*i+j], end = ' ')
    print()
