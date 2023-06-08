
arr = list(input())
bomb = list(input())

stack = []
# print(arr)

for i in range(len(bomb)):
    stack.append(arr[i])
# print(stack)

# count = len(bomb)

count = 0
inputidx = len(bomb)-1
idx = -1
while True:
    if stack[idx] == bomb[idx]:
        idx -= 1
        count += 1
    else:
        idx = -1
        count = 0
        inputidx += 1
        if inputidx == len(arr):
            break
        stack.append(arr[inputidx])
    if count == len(bomb):
        for i in range(len(bomb)):
            stack.pop()
        # print(stack)
        idx = -1
        count = 0
        inputidx += 1
        if inputidx == len(arr):
            break
        stack.append(arr[inputidx])


if stack:
    print(*stack, sep='')
else:
    print('FRULA')
