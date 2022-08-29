T = int(input())
prime_list = [2, 3, 5, 7, 11]

for i in range(T):
    cnt_list = [0]*5
    N = int(input())
    for j in range(len(prime_list)):
        while True:
            # print(N)
            if N % prime_list[j] != 0:
                break
            else:
                N /= prime_list[j]
                cnt_list[j] += 1
    print(f'#%d'%(i+1), end=' ')

    print(*cnt_list, sep = ' ')
