T = int(input())

for i in range(T):
    K, N, M = list(map(int, input().split()))

    M_list = list(map(int, input().split()))
    M_list.insert(0, 0)
    M_list.append(N)

    st = 0
    end = 1
    cnt = 0
    while True:


        if end-st == 1 and M_list[end] - M_list[st] > K:
            cnt = 0
            break

        if M_list[end] - M_list[st] > K:
            # print(M_list[st], M_list[end])
            st += 1

        else:
            # print(M_list[st], M_list[end])
            if M_list[end] == N:
                break
            elif M_list[end+1] - M_list[st] > K:
                cnt += 1
                st = end
                end += 1
            else:
                end += 1
            # print(cnt)


    print(f'#%d %d' %(i+1, cnt))
