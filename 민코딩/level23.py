# 민코딩 level 23 1번
# people = list(input())
# gift_list = [0]*3
# used_list = [0]*4
#
# def abc(level):
#     if level == 3:
#         for i in range(level):
#             print(gift_list[i], end='')
#         print()
#         return
#     for j in range(len(people)):
#         if used_list[j] == 1: continue
#         gift_list[level] = people[j]
#         used_list[j] = 1
#         abc(level+1)
#         used_list[j] = 0
# result = abc(0)

# 민코딩 level 23 2번
# word = list(input())
# word_list = [0]*4
# cnt = 0
# def abc(level):
#     global cnt
#     if level == 4:
#         cnt += 1
#
#         return
#     for i in range(len(word)):
#         if level > 0 and (word_list[level-1] == 'B' and word[i] == 'T') or (word_list[level-1] == 'T' and word[i] == 'B'):
#             continue
#         word_list[level] = word[i]
#         abc(level+1)
#
# result = abc(0)
#
# print(cnt)

# 민코딩 level 23 3번
# n = int(input())
# word_list = ['A', 'B', 'C']
# chosen_list = [0]* n
#
# cnt = 0
# def abc(level):
#     global cnt
#     if level == n:
#         cnt += 1
#         return
#
#     for j in range(len(word_list)):
#         if level > 1 and chosen_list[level-1] == chosen_list[level-2] == word_list[j]: continue
#         chosen_list[level] = word_list[j]
#
#         abc(level+1)
#
# result = abc(0)
# print(cnt)

# 민코딩 level 23 4번
# n = int(input())
# word_list = ['B', 'T', 'S', 'K', 'R']
# chosen_list = [0]* n
# used_list = [0]*5
# cnt = 0
# def abc(level):
#     global cnt
#     if level == n:
#         if 'S' in chosen_list:
#             cnt += 1
#         return
#
#     for j in range(len(word_list)):
#         if used_list[j] == 1: continue
#         chosen_list[level] = word_list[j]
#         used_list[j] = 1
#         abc(level+1)
#         used_list[j] = 0
#
#
# result = abc(0)
# print(cnt)

# 민코딩 level 23 5번
# N = input()
# word_list = ['E', 'W', 'A', 'B', 'C']
# chosen_list = [0]*4
# used_list = [0]*5
# def abc(level):
#     if level == 4:
#         for i in range(4):
#             print(chosen_list[i], end='')
#         print()
#         return
#
#     for j in range(len(word_list)):
#         if word_list[j] == N: continue
#         if used_list[j] == 1: continue
#         chosen_list[level] = word_list[j]
#         used_list[j] = 1
#         abc(level+1)
#         used_list[j] = 0
#
#
# result = abc(0)

# 민코딩 level 23 6번
A = list(map(int, input()))

choose = [0]*4
cnt = 0
def abc(level):
    global cnt
    if level == 4:
        cnt += 1
        return

    for i in range(len(A)):
        if level > 0 and abs(choose[level-1]-A[i]) > 3: continue
        choose[level] = A[i]
        abc(level+1)

result = abc(0)

print(cnt)