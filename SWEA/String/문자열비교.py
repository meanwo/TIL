T = int(input())

for i in range(T):
    flag = 0
    str1, str2 = [list(input()) for _ in range(2)]

    for j in range(len(str2)-len(str1)+1):
        if str1 == str2[j:j+len(str1)]:
            flag = 1
            break
    if flag == 1:
        print(f'#%d %d' %(i+1, 1))
    else:
        print(f'#%d %d' % (i + 1, 0))