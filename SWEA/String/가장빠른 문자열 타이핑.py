T = int(input())
for i in range(T):

    word, part = input().split()
    cnt = 0
    flag = 1
    while flag:
        if part not in word:
            cnt += len(word)
            print(f'#%d %d' %(i+1, cnt))
            flag = 0
        else:
            word = word.replace(part, '', 1)
            # print(word)
            cnt += 1