def findboss(member):
    global arr
    if arr[member] == 0:
        return member
    ret = findboss(arr[member])
    arr[member] = ret
    return ret


def union(a, b):
    global arr
    aboss=findboss(a)
    bboss=findboss(b)
    if aboss==bboss:
        return
    arr[bboss]=aboss
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [0]*(N+1)

    num = list(map(int, input().split()))
    num_list =[]
    for i in range(0, M*2, 2):
        num_list.append([num[i], num[i+1]])


    for i in range(len(num_list)):
        union(num_list[i][0], num_list[i][1])
    boss_list = []
    for i in range(1, N+1):
        if findboss(i) not in boss_list:
            boss_list.append(findboss(i))
    # print(arr)
    cnt = len(boss_list)
    print(f'#%d %d' %(test_case, cnt))
