R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
# print(arr)

new_arr = [[0]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        new_arr[i][j] = arr[i][j]
# print()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(R):
    for j in range(C):
        cnt = 0
        if arr[i][j] == 'X':
            if i == 0:
                cnt += 1
            if i == R-1:
                cnt += 1
            if j == 0:
                cnt += 1
            if j == C - 1:
                cnt += 1
            for k in range(4):
                if 0 <= i+dy[k] <= R-1 and 0 <= j+dx[k] <= C-1 and arr[i+dy[k]][j+dx[k]] == '.':
                    cnt += 1
            if cnt >= 3:
                new_arr[i][j] = '.'
row_list = []
col_list = []
for i in range(R):
    for j in range(C):
        if new_arr[i][j] == 'X':
            row_list.append(i)
            col_list.append(j)

min_row = min(row_list)
max_row = max(row_list)
min_col = min(col_list)
max_col = max(col_list)

for i in range(min_row, max_row+1):
    for j in range(min_col, max_col+1):
        print(new_arr[i][j], end ='')
    if i != max_row:
        print()
