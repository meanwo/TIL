col_list = ['1', '2', '3', '4', '5', '6']
row_list = ['A', 'B', 'C', 'D', 'E', 'F']
visited_arr = [[0]*6 for _ in range(6)]

command_list = []
for i in range(36):
    a = list(input())
    command_list.append(a)

for i in range(36):
    row = row_list.index(command_list[i][0])
    col = col_list.index(command_list[i][1])
    visited_arr[row][col] += 1

# print(visited_arr)
flag = 1

# print(command_list[36%len(command_list)][0])
def check_move(command_list, flag):
    for i in range(len(command_list)):
        if abs(row_list.index(command_list[i][0]) - row_list.index(command_list[(i+1)%len(command_list)][0])) == 2 and abs(
                col_list.index(command_list[i][1]) - col_list.index(command_list[(i+1)%len(command_list)][1])) == 1:
            continue
        elif abs(row_list.index(command_list[i][0]) - row_list.index(command_list[(i+1)%len(command_list)][0])) == 1 and abs(
                col_list.index(command_list[i][1]) - col_list.index(command_list[(i+1)%len(command_list)][1])) == 2:
            continue
        else:
            flag = 0
            break
    return flag
for i in range(6):
    for j in range(6):
        if visited_arr[i][j] != 1:
            flag = 0
            break
    if flag == 0:
        break


if flag == 1:
    flag = check_move(command_list, flag)


if flag == 1:
    print('Valid')
else:
    print('Invalid')