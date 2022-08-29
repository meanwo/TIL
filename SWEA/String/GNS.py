num_str = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
T = int(input())
for i in range(T):
    cnt_list = [0]*10
    n_proto = input()
    n = int(n_proto[3:])
    n_list = list(input().split())
    ordered_list = [0]*n

    for j in range(n):
        cnt_list[num_str.index(n_list[j])] += 1

    for j in range(1, 10):
        cnt_list[j] += cnt_list[j-1]

    for j in range(n):
        ordered_list[cnt_list[num_str.index(n_list[j])]-1] = n_list[j]
        cnt_list[num_str.index(n_list[j])] -= 1
    print(f'#%d' %(i+1))
    print(*ordered_list, sep = ' ')
