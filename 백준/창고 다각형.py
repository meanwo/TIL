n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

order_list = sorted(arr, key=lambda x: x[0])
# print(order_list)

max_index = 0

for i in range(n):
    if arr[i][1] > order_list[max_index][1]:
        max_index = i
# print(max_index)
max_xy = order_list[max_index]

idx1 = max_index
idx2 = max_index
# max_index_left = 0
# max_index_right = n-1
# box_list = []
# box_list.append(order_list[max_index])
sum_rec = order_list[max_index][1]
while True:
    if idx1 == 0:
        break
    max_index_left = idx1-1
    for i in range(idx1):
        if order_list[i][1] > order_list[max_index_left][1]:
            max_index_left = i
    # box_list.append(order_list[max_index_left])

    sum_rec += (order_list[idx1][0]-order_list[max_index_left][0])*order_list[max_index_left][1]

    idx1 = max_index_left
    # print(idx1)
#
#

while True:
    if idx2 == n-1:
        break
    max_index_right = idx2+1
    for i in range(idx2+1, n):
        if order_list[i][1] > order_list[max_index_right][1]:
            max_index_right = i
    # box_list.append(order_list[max_index_right])

    sum_rec += (order_list[max_index_right][0] - order_list[idx2][0]) * order_list[max_index_right][1]
    idx2 = max_index_right
    # print(idx2)
#
# # print(box_list)
#
print(sum_rec)