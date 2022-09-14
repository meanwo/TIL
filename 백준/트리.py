# arr 안에 index와 같은 원소가 있다면 리프노드가 아님.

N = int(input())
arr = list(map(int, input().split()))
target = int(input())

cnt = 0
remove_list = []
for i in range(N):
    # if arr[i] == -1:
    #     continue
    if target == arr[i]:
        # remove_list.append(target)
        remove_list.append(i)
        continue
    if arr[i] in remove_list:
        remove_list.append(i)
        continue
    if i == target:
        continue
    if i in arr and arr[target] != i:
        remove_list.append(target)
        continue
    cnt += 1

remove_list = list(set(remove_list))
if len(remove_list) == N-1:
    cnt += 1
print(remove_list)
print(cnt)