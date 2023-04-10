import sys
arr = sys.stdin.readline()


sym_example = ['+', '-']
num_list = []
sym_list = []

idx = 0

# 숫자와 수식 분리
for i in range(len(arr)):
    if arr[i] in sym_example:
        num_list.append(int(arr[idx:i]))
        sym_list.append(arr[i])
        idx = i+1
    if i == len(arr)-1:
        num_list.append(int(arr[idx::]))
# print(num_list)
# print(sym_list)


# - 부호가 최초로 나온 이후로는 괄호를 통해 모두 음수로 만들 수 있다.
result = num_list[0]
flag = 0
for i in range(len(sym_list)):
    if sym_list[i] == '-' or flag == 1:
        result -= num_list[i+1]
        flag = 1
    elif sym_list[i] == '+':
        result += num_list[i+1]

print(result)