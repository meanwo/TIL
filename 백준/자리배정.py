C, R = map(int, input().split())
target = int(input())
arr = [[0]*C for _ in range(R)]

now_dir = 0
row = R-1
col = 0
num = 1
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

while True:
    if C * R < target:
        print(0)
        break
    if num == target:
        print(col+1, R-row)
        break
    arr[row][col] = num
    next_row = row + dy[now_dir]
    next_col = col + dx[now_dir]
    if next_col < 0 or next_row < 0 or next_col >= C or next_row >= R or arr[next_row][next_col] != 0:
        now_dir = (now_dir+1) % 4
        next_row = row + dy[now_dir]
        next_col = col + dx[now_dir]

    row = next_row
    col = next_col
    num += 1
