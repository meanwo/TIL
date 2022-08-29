T = int(input())
for j in range(T):
    oven_ch = []
    oven_pz = []
    N, M = map(int, input().split())
    cheese_list = list(map(int, input().split()))
    pizza_list = [i for i in range(1, M+1)]
    for i in range(N):
        oven_ch.append(cheese_list.pop(0))
        oven_pz.append(pizza_list.pop(0))

    while True:
        oven_ch.append(oven_ch.pop(0))
        oven_pz.append(oven_pz.pop(0))
        oven_ch[N-1] //= 2
        if oven_ch[N-1] == 0 and len(cheese_list) != 0:
            oven_ch[N-1] = cheese_list.pop(0)
            oven_pz[N-1] = pizza_list.pop(0)

        if oven_ch.count(0) == N-1:
            break

    for i in range(len(oven_ch)):
        if oven_ch[i] != 0:
            last_index = i

    print(f'#%d %d' %(j+1, oven_pz[last_index]))

