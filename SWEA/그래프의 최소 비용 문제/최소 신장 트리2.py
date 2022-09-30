# union 함수
def union(a, b):
    global sum_cost, cnt

    fa,fb=findboss(a), findboss(b)
    if fa == fb:return 0
    arr[fb]=fa
    return 1



def findboss(member):
    global arr
    if arr[member] == member:
        return member
    ret = findboss(arr[member])
    arr[member]=ret
    return ret

T = int(input())

for test_case in range(1, T+1):
    sum_cost = 0
    cnt = 0

    V, E = map(int, input().split())
    arr = list(range(V + 1))
    info_list = []
    for i in range(E):
        a, b, cost = map(int, input().split())
        info_list.append([a, b, cost])
    sort_list = sorted(info_list, key=lambda x: x[2])

    for i in range(E):
        if union(sort_list[i][0], sort_list[i][1]) == 1:
            cnt += 1
            sum_cost += sort_list[i][2]


    print(f'#%d %d' %(test_case, sum_cost))