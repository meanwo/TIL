# union 함수
def union(a,b):
    global arr

    fa,fb=findboss(a), findboss(b)
    if fa == fb:return 1
    arr[fb]=fa


# 최소 비용 구하는 함수
def minumum_cost(E):
    global sort_list, sum_cost, cnt
    for i in range(E):
        a, b = sort_list[i][0], sort_list[i][1]
        ret = union(a, b)
        if ret == 1:
            continue
        if cnt == V:
            break
        cnt += 1
        sum_cost += sort_list[i][2]

def findboss(member):
    global arr
    if arr[member] == 0:
        return member
    ret = findboss(arr[member])
    arr[member]=ret
    return ret

T = int(input())

for test_case in range(1, T+1):
    sum_cost = 0
    cnt = 0

    V, E = map(int, input().split())
    arr = [0]*(V+1)
    info_list = []
    for i in range(E):
        a, b, cost = map(int, input().split())
        info_list.append([a, b, cost])
    sort_list = sorted(info_list, key=lambda x: x[2])

    result = minumum_cost(E)
    print(f'#%d %d' %(test_case, sum_cost))