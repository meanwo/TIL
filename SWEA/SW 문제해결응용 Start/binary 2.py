T = int(input())
for test_case in range(1, T+1):
    N = float(input())
    array = []
    for i in range(1, 13):

        if N >= 2**(-i):
            N -= 2**(-i)
            array.append(1)
        else:
            array.append(0)
        if i == 12 and N != 0:
            print(f'#%d overflow' % test_case)
        if N == 0:
            print(f'#%d' % test_case, end=' ')
            print(*array, sep='')
            break
