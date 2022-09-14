for test_case in range(1, 11):
    N = int(input())
    leftson = [0]*(N+1)
    rightson = [0]*(N+1)
    word_list = [0]*(N+1)
    for i in range(1, N+1):
        N_list = list(input().split())
        word_list[i] = N_list[1]
        N_list[0] = int(N_list[0])
        if len(N_list) >= 3:
            N_list[2] = int(N_list[2])
            leftson[N_list[0]] = N_list[2]
            if len(N_list) == 4:
                N_list[3] = int(N_list[3])
                rightson[N_list[0]] = N_list[3]
    # print(N_list)
    # print(word_list)

    print(f'#%d' %test_case, end= ' ')
    def inorder(n):
        if n:
            inorder(leftson[n])
            print(word_list[n], end= '')
            inorder(rightson[n])

    result = inorder(1)
    print()

