# 민코딩 level 23.5 1번
# A = [3, 5, 1, 9, 7]
#
# for i in range(4):
#     RL = input()
#     if RL == 'R':
#         A.insert(0, A.pop())
#     elif RL == 'L':
#         k = A.pop(0)
#
#         A.append(k)
#
# print(*A)

# 민코딩 level 23.5 2번

# location = [list(map(int, input().split())) for _ in range(3)]
#
# flag = 1
# for i in range(2):
#     cnt_list = [0] * 100
#     for j in range(3):
#         cnt_list[location[j][i]] += 1
#
#     for j in range(3):
#         if cnt_list[j] > 1:
#             flag = 0
#
# if flag == 1:
#     print("안전")
# else:
#     print("위험")

# 민코딩 level 23.5 3번
# arr = [[0]*4 for _ in range(4)]
# input_arr = [list(map(int, input().split())) for _ in range(3)]
#
# for i in range(3):
#     for j in range(3):
#         arr[i][j] = input_arr[i][j]

# for i in range(3):
#     for j in range(3):
#         arr[3][j] += arr[i][j]
#         arr[i][3] += arr[i][j]
#
# for i in range(3):
#     arr[3][3] += arr[i][i]
#
# for i in range(4):
#     for j in range(4):
#         print(arr[i][j], end=' ')
#     print()

# 민코딩 level 23.5 4번
# arr = [[3, 5, 4, 1], [1, 1, 2, 3], [6, 7, 1, 2]]
# change = list(map(int, input().split()))
# change_2 = change[0:4]
# change_2.append(change_2.pop(0))
#
# for i in range(3):
#     for j in range(4):
#         for k in range(4):
#             if arr[i][j] == change[k]:
#                 arr[i][j] = change_2[k]
#                 break
#
# for i in range(3):
#     print(*arr[i], sep= ' ')

# 민코딩 level 23.5 5번
# arr = list(map(int, input().split()))
#
# a = 0
# b = 7
# while True:
#     if a > b:
#         arr[0], arr[b] = arr[b], arr[0]
#         break
#     if arr[a] > arr[0] and arr[b] < arr[0]:
#         arr[a], arr[b] = arr[b], arr[a]
#     elif arr[a] <= arr[0]:
#         a += 1
#     elif arr[b] >= arr[0]:
#         b -= 1
#
# print(*arr, sep = ' ')

# 민코딩 level 23.5 6번

left_arr = [list(input()) for _ in range(4)]
right_arr = [['A', 'B', 'C', 'D'], ['B', 'B', 'A', 'B'], ['C', 'B', 'A', 'C'], ['B', 'A', 'A', 'A']]

cnt_dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
# cnt_dict['A'] = 1
# print(cnt_dict)
#
for i in range(4):
    for j in range(4):
        if left_arr[i][j] == right_arr[i][j]:
            cnt_dict[left_arr[i][j]] += 1
# print(cnt_dict)
print(max(cnt_dict, key = cnt_dict.get))


