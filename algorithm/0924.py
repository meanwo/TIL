# def solution(today, terms, privacies):
#     answer = []
#     terms_dict = {}
#     for i in range(len(privacies)):
#         start_info = privacies[i].split()
#         start_year = start_info[0].split('.')[0]
#         start_month = start_info[0].split('.')[1]
#         start_date = start_info[0].split('.')[2]
#         spec = start_info[1]
#         # print(start_info, start_year)
#         print(start_year, start_month, start_date, spec)
#     for i in range(len(terms)):
#         terms = list(terms.split())
#     return answer

# test_arr = [[8, 4], [3, 3], [14, 1], []]
#
# print(max(test_arr)[0])
#
# result = 0
# for i in range(len(test_arr)):
#     if len(test_arr[i]) != 0:
#         result += (test_arr[i][0])
#
# print(result)

next_arr = [[[], [[3, 2]], [], [], [], [], []], [[], [[7, 1]], [], [], [], [], []], [[], [], [], [], [], [[8, 2], [100, 1]], []], [[], [], [], [[8, 4], [3, 3], [14, 1]], [], [], []], [[], [], [], [], [], [[1, 1]], []], [[], [], [[5, 4]], [], [], [], []], [[], [], [], [], [], [], []]]

for j in range(7):
    for k in range(7):
        if len(next_arr[j][k]) != 0:
            new_dir = max(next_arr[j][k])[1]
            part_total = 0
            for l in range(len(next_arr[j][k])):
                part_total += next_arr[j][k][l][0]
            next_arr[j][k] = [part_total, new_dir]
        else:
            next_arr[j][k] = [0, 0]
print(next_arr)
