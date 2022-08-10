# 민코딩 level 18 1번
# id = [[65000, 35, 42, 70], [70, 35, 65000, 1300], [65000, 30000, 38, 42]]
# id_table = []
# for i in range(3):
#     for j in range(4):
#         id_table.append(id[i][j])
#
# address_table = [0]*65001
#
# # print(len(address_table))
# for i in range(len(id_table)):
#     address_table[id_table[i]] += 1
#
# max_factor = address_table[0]
#
# for i in range(len(address_table)):
#     if address_table[i] > max_factor:
#         max_factor = address_table[i]
# print(address_table.index(max_factor))

# 민코딩 level 18 2번
# A = [list(map(int, input().split())) for _ in range(3)]
# A_list = []
# A_count = [0]*9
# empty_number = []
# for i in range(3):
#     for j in range(3):
#         A_list.append(A[i][j])
#
# # 1의 갯수는 A_count의 0번째 인덱스에 저장
# for i in range(9):
#     A_count[A_list[i]-1] += 1
#
# # 해당 요소가 0인 인덱스를 추출
# for i in range(9):
#     if A_count[i] == 0:
#         empty_number.append(i+1)
#
# print(*empty_number, sep = ' ')

# 민코딩 level 18 3번
# A = [[1, 3, 3, 5, 1], [3, 6, 2, 4, 2], [1, 9, 2, 6, 5]]
# A_list = []
# A_count = [0]*16
# result =[]
# n = int(input())
#
# for i in range(3):
#     for j in range(5):
#         A_list.append(A[i][j])
#
# for i in range(15):
#     A_count[A_list[i]] += 1
#
# for i in range(15):
#     if A_count[i] == n:
#         result.append(i)
#
# print(*result, sep=' ')

# 민코딩 level 18 4번
# CardList = list(input())
#
# ord_cardlist = []
# count_list = [0]*100
# cnt = 0
# for i in range(len(CardList)):
#     ord_cardlist.append(ord(CardList[i]))
#     count_list[ord_cardlist[i]] += 1
#
# for i in range(len(count_list)):
#     if count_list[i] >= 1:
#         cnt += 1
#
# print(f"%d개" %cnt)

# 민코딩 level 18 5번
# S = list(input())
# ord_S_list = []
# count_list = [0]*100
# max_S = 0
# for i in range(len(S)):
#     ord_S_list.append(ord(S[i]))
#     count_list[ord_S_list[i]] += 1
#
# for i in range(len(count_list)):
#     if count_list[i] > max_S:
#         max_S = count_list[i]
#         max_index = i
# print(chr(max_index))

# 민코딩 level 18 6번
# town = [['C', 'D', 'A'], ['B', 'M', 'Z'], ['Q', 'P', 'O']]
# black = list(input())
# cnt = 0
# town_list = []
# for i in range(3):
#     for j in range(3):
#         town_list.append(town[i][j])
#
# for i in range(len(town_list)):
#     if town_list[i] in black:
#         cnt += 1
#
# print(f'%d명' %cnt)

# # 민코딩 level 18 7번
# alphabet = [['A', 'B', 'C'], ['A', 'G', 'H'], ['H', 'I', 'J'], ['K', 'A', 'B'], ['A', 'B', 'C']]
#
# alphabet_list = []
# ord_alphabet_list = []
# asci_alphabet = [0]*100
# sorted_list = [0]*100
#
# final_result =[]
# for i in range(5):
#     for j in range(3):
#         alphabet_list.append(alphabet[i][j])
#
# # DAT 만들기
# for i in range(len(alphabet_list)):
#     ord_alphabet_list.append(ord(alphabet_list[i]))
#     asci_alphabet[ord_alphabet_list[i]] += 1
#
# # 누적합 만들기
# for i in range(1, len(asci_alphabet)):
#     asci_alphabet[i] += asci_alphabet[i-1]
#
# # 정렬하기
# for i in range(len(ord_alphabet_list)):
#     index = ord_alphabet_list[i]
#     sorted_list[asci_alphabet[index]-1] = ord_alphabet_list[i]
#     asci_alphabet[ord_alphabet_list[i]] -= 1
#
# for i in range(len(sorted_list)):
#     if sorted_list[i] > 0:
#         final_result.append(chr(sorted_list[i]))
#
# print(*final_result, sep ='')

# 민코딩 level 18 8번
# train = [3, 7, 6, 4, 2, 9, 1, 7]
#
# team = list(map(int, input().split()))
#
# for i in range(len(train)-2):
#     if train[i:i+3] == team:
#         print(f'%d번~%d번 칸' %(i, i+2))

# # 민코딩 level 18 9번
# apartment = [[15, 18, 17], [4, 6, 9], [10, 1, 3], [7, 8, 9], [15, 2, 6]]
#
# floor = list(map(int, input().split()))
#
# def isPattern():
#     for i in range(len(apartment)):
#         if apartment[i] == floor:
#             print(f'%d층' %((len(apartment)-i)))
#
# get_floor = isPattern()
# get_floor


