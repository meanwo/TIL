T=int(input())

for tc in range(1, 1+T):

    arrs = list(input())

    lst = []
    op = ["{", "("]

    result = 1
    for arr in arrs:
        if arr in op:
            lst.append(arr)

        elif arr == ")":
            if len(lst) == 0:
                result = 0
                break
            elif lst[-1] == "(":
                lst.pop()

        elif arr == "}":
            if len(lst) == 0:
                result = 0
                break
            elif lst[-1] == "{":
                lst.pop()



    if len(lst) != 0:
        result = 0

    print(f'#{tc} {result}')
