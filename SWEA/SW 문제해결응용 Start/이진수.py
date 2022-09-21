def bit_print(i):
    s = ''
    for j in range(3, -1, -1):
        s += '1' if (i & (1 << j)) else '0'
    print(s, end='')
h_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


T = int(input())
for test_case in range(1, T+1):
    N, h = list(input().split())
    N = int(N)

    print(f'#%d' %test_case, end=' ')

    for i in range(N):
        bit_print(h_list.index(h[i]))
    print()
