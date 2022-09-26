T = int(input())
for test_case in range(1, T+1):
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    count_list = [0, 0, 0, 0, 0, 0, 0, 0]
    N = int(input())


    for i in range(len(money_list)):
        count_list[i] = N // money_list[i]
        N = N % money_list[i]
    print(f'#%d' %test_case)
    print(*count_list)