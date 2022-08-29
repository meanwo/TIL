n = int(input())

max_len = 0

for i in range(1, n+1):
    n_list = [n, i]
    while True:
        new_n = n_list[-2] - n_list[-1]
        if new_n >= 0:
            n_list.append(new_n)
        elif new_n < 0:
            if len(n_list) > max_len:
                max_len = len(n_list)
                max_list = n_list
                break
            else:
                break
print(max_len)
print(*max_list, sep = ' ')