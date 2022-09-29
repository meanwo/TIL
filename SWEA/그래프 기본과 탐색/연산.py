def find_num(target):
    queue = [N]
    used_list = [0]*1000001
    used_list[N] = 1
    cnt = 0
    while queue:
        cnt += 1
        num = queue.pop(0)
        print(num)
        if num == target:
            return cnt
        new_num = [num+1, num-1, num*2, num-10]
        for i in range(4):
            if new_num[i] > 1000000: continue
            if new_num[i] < 1: continue
            if used_list[new_num[i]] == 1: continue
            used_list[new_num[i]] = 1
            queue.append([new_num[i]])
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    print(f'#%d %d' %(test_case, find_num(M)))