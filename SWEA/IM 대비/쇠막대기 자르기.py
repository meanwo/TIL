T = int(input())
for test_case in range(1, T+1):
    arr = list(input())
    layer = 0
    cnt = 0
    index = 0
    while True:
        if index == len(arr):
            break

        if arr[index] == '(':
            if arr[index+1] == ')':
                index += 2
                cnt += layer
            else:
                index += 1
                layer += 1
                cnt += 1
        else:
            index += 1
            layer -= 1


    print('#%d %d' %(test_case, cnt))


