

# T = int(input())
# for test_case in range(1, T+1):
#     N, B = map(int, input().split())
#     height = list(map(int, input().split()))
#
#     height.sort(reverse=True)
#     total = 0
#     for i in range(N):
#         total += height[i]
#
#         if total == B:
#             print(f'#%d %d' % (test_case, 0))
#         elif total > B:
#
#
#     print(f'#%d %d' %(test_case, min_dif))

def backtracking(start, total):
    global min_dif

    if total >= B:
        if min_dif > total - B:
            min_dif = total - B
        return
    elif total-B > min_dif:
        return

    for i in range(start, N):
        if used[i] == 0:
            used[i] = 1
            backtracking(i+1, total+height[i])
            used[i] = 0

T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    height.sort()
    min_dif = 99999
    used = [0]*N

    backtracking(0, 0)
    print(f'#%d %d' %(test_case, min_dif))