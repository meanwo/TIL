T = int(input())
for i in range(T):
    n = int(input())
    card_list = list(map(int, input()))
    cnt_list = [0]*10

    max_num = 0
    max_index = 0
    for j in range(n):
        cnt_list[card_list[j]] += 1
    for j in range(len(cnt_list)):
        if max_num <= cnt_list[j]:
            max_num = cnt_list[j]
            max_index = j
    print(f'#%d %d %d' %(i+1, max_index, max_num))