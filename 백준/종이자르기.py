col, row = map(int, input().split())
n = int(input())

row_list = [0, row]
col_list = [0, col]

for i in range(n):
    dir, index = map(int, input().split())
    if dir == 0:
        row_list.append(index)
    elif dir == 1:
        col_list.append(index)

row_list.sort()
col_list.sort()

max_row = 0
max_col = 0
for i in range(1, len(row_list)):
    len_row = row_list[i]- row_list[i-1]
    if len_row > max_row:
        max_row = len_row
for i in range(1, len(col_list)):
    len_col = col_list[i] - col_list[i-1]
    if len_col > max_col:
        max_col = len_col
print(max_col*max_row)