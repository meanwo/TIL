#  r: 총 페이지, target: 구하고자 하는 수, cnt: 탐색에 걸리는 횟수
def find_num(l, r, target, cnt):

    if int((l+r)/2) == target:
        cnt += 1
        # print(cnt)
        return cnt

    if int((l+r)/2) < target:
        cnt += 1
        l = int((l+r)/2)
        return find_num(l, r, target, cnt)

    elif int((l+r)/2) > target:
        cnt += 1
        r = int((l+r)/2)
        return find_num(l, r, target, cnt)

T = int(input())
for i in range(T):
    N = list(map(int, input().split()))
    result_a = find_num(1, N[0], N[1], 0)
    # print(result_a)
    result_a
    # print(type(result_a))
    result_b = find_num(1, N[0], N[2], 0)
    # print(result_b)
    result_b

    if result_a < result_b:
        print(f'#%d %s' %(i+1, 'A'))
    elif result_a > result_b:
        print(f'#%d %s' %(i+1, 'B'))
    else:
        print(f'#%d %d' %(i+1, 0))


