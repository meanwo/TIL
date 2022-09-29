T = int(input())
for test_case in range(1, T+1):
    num, cnt = list(input().split())
    num = list(map(int, num))
    cnt = int(cnt)
    duple = 0
    duple2 = 0
    idx = 0
    while cnt:
        if idx >= len(num)-1:
            num[-1], num[-2] = num[-2], num[-1]
            cnt -= 1
        elif num[idx] >= max(num[idx+1:]):
            if num[idx] == max(num[idx+1:]):
                duple2 += 1
            idx += 1
        else:
            max_num = -1
            max_index = 0
            for i in range(len(num)-1, idx, -1):
                duple = 0
                if max_num < num[i]:
                    max_num = num[i]
                    max_index = i
                elif max_num == num[i]:
                    duple += 1
            num[idx], num[max_index] = num[max_index], num[idx]
            if duple >= 1:
                part = []
                for i in range(duple+1):
                    part.append(num.pop())
                part.sort(reverse=True)

                for i in range(len(part)):
                    num.append(part[i])
            cnt -= 1
            idx += 1
        if duple2 >= 1:
            part2 = []
            for i in range(duple2+1):
                part2.append(num.pop())
            part2.sort(reverse=True)

            for i in range(len(part2)):
                num.append(part2[i])

    print(f'#%d' %test_case, end=' ')
    print(*num, sep='')
