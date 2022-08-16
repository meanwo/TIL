#  1 누적합 구하기 (재귀 들어가면서 누적합 출력하기)

# arr=[3,4,5,1,6,9]
# sum=3
# def abc(level):
#     global sum
#     if level==5:
#         print(sum)
#         return
#     print(sum)
#     sum+=arr[level+1]
#     abc(level+1)
# abc(0)

# def abc(level,sum):
#     if level==5:
#         print(sum)
#         return
#     print(sum)
#     abc(level+1,sum+arr[level+1])
#
# abc(0,3) # level sum


# # 2 그전에는 누적합을 3 7 12 13 19 28 이렇게 출력 했다면..
# # 이번에는 28 19 13 12 7 3
#
# arr=[3,4,5,1,6,9]
# #
# # def abc(level,sum):
# #     if level==5:
# #         print(sum)
# #         return
# #     abc(level+1,sum+arr[level+1])
# #     print(sum)
# #
# # abc(0,3)
#
# sum=3
#
# def abc(level):
#     global sum
#     if level==5:
#         print(sum)
#         return
#     sum+=arr[level+1]
#     abc(level+1)
#     sum-=arr[level+1]
#     print(sum)
#
# abc(0)

#3

# arr = [5, 9, 7, 3, 1, 5, 6, 4]

# sum = 5
# def abc(level, sum):
#     print(sum)
#     if level == 7:
#         return
#     abc(level+1, sum+arr[level+1])
#     print(sum)
# result = abc(0, sum)
# result

# sum = 5
# def abc(level):
#     global sum
#     print(sum)
#     if level == 7:
#         return
#     sum += arr[level+1]
#     abc(level+1)
#     sum -= arr[level+1]
#     print(sum)
#
# result = abc(0)

#  개구리 점프 문제
# arr = [2, 0, 1, 1, 3, 5, 1]
# def abc(level):
#     if level > 6:
#         return
#     abc(level+arr[level])
#     print(arr[level])
#
# result = abc(0)

# 카드를 3장 뽑았을 때 나올 수 있는 합의 경우의 수를 모두 구하시오
# 매개변수 이용 방법

# arr = [3, 7, 1, 5]
#
# sum = 0
# def abc(level, sum):
#     if level == 3:
#         print(sum, end=' ')
#         return
#     for i in range(4):
#
#         abc(level+1, sum+arr[i])
#
# result = abc(0, 0)

# # 전역변수 이용 방법
# sum = 0
# def abc(level):
#     global sum
#     if level == 3:
#         print(sum, end= ' ')
#         return
#     for i in range(4):
#         sum += arr[i]
#         abc(level+1)
#         sum -= arr[i]
#
# result = abc(0)

# 4번 카드를 뽑아서 합이 10이상인 경우의 갯수 구하기
# arr = [4, -7, 1, 3]
# cnt = 0
# def abc(level, sum):
#     global cnt
#     if level == 4:
#         if sum > 10:
#             cnt += 1
#             print(sum, end= ' ')
#         return
#     for i in range(4):
#         abc(level+1, sum+arr[i])
#
#
# result = abc(0, 0)
# print()
# print(cnt)

# 거스름 돈
# n = int(input())
# coin = [100, 70, 10]
# min_level = 9999
# def abc(level, sum):
#     global min_level
#     if sum > n:
#         return
#     elif sum == n:
#         if min_level > level:
#             min_level = level
#         return
#     for i in range(3):
#         abc(level+1, sum+coin[i])
#
# result = abc(0, 0)
#
# print(min_level)

# card = ['A', 'B', 'C']
# card_list = [0]*2
# def abc(level, card_list):
#     # global card_list
#     if level == 2:
#         for i in range(level):
#             print(card_list[i], end=' ')
#         print()
#         return
#     for i in range(3):
#         card_list[level] = (card[i])
#         abc(level+1, card_list)
#         # print(card_list)
#
# result = abc(0, card_list)
#

# n개의 주사위를 던져서 나오는 결과 출력
# dice = [1, 2, 3, 4, 5, 6]
# n = int(input())
# dice_list = [0]*n
# def abc(level, dice_list):
#     if level == n:
#         for i in range(level):
#             print(dice_list[i], end = ' ')
#         print()
#         return
#     for j in range(6):
#         dice_list[level] = dice[j]
#         abc(level+1, dice_list)
#
# rresult = abc(0, dice_list)


# n개의 주사위를 던져서 나오는 결과 출력( 중복 제거)
# n = int(input())
# dice = [1, 2, 3, 4, 5, 6]
# dice_list = [0]*n
# used = [0]*6
#
# def abc(level):
#     if level == n:
#         for i in range(n):
#             print(dice_list[i], end = ' ')
#         print()
#         return
#     for j in range(6):
#         if used[j] ==1: continue
#         dice_list[level] = dice[j]
#         used[j] = 1
#         abc(level+1)
#         used[j] = 0
#         # dice_list[level] =0
#
# result = abc(0)

#ABCD 중  금은동 경우의수 구하기
# arr= ['A', 'B', 'C', 'D']
# medal_list = [0]*3
# used = [0]*4
# def abc(level):
#     if level == 3:
#         for i in range(level):
#             print(medal_list[i], end = ' ')
#         print()
#         return
#     for i in range(4):
#         if used[i] == 1:continue
#         medal_list[level] = arr[i]
#         used[i] = 1
#         abc(level+1)
#         used[i] = 0
# result = abc(0)


# AAA~DDD까지의 중복순열 중 C로 시작하는 순열은 제외하고 출력하기

# arr = ['A', 'B', 'C', 'D']
# alphabet_list = [0]*3
# def abc(level):
#     if level == 1 and alphabet_list[level-1] == 'C':
#         return
#     if level == 3:
#         for i in range(level):
#             print(alphabet_list[i], end= ' ')
#         print()
#         return
#     for i in range(4):
#         # if alphabet_list[i] == 'C' and level == 0:
#         #     continue
#         alphabet_list[level] = arr[i]
#         abc(level+1)
#
# result = abc(0)


# AAA~DDD까지의 중복순열 중 B로 시작하는 순열은 제외하고 출력하기
# arr = ['A', 'B', 'C', 'D']
# alphabet_list = [0]*3
#
# def abc(level):
#     if level > 0 and alphabet_list[level-1] =='B': return
#     if level == 3:
#         for j in range(level):
#             print(alphabet_list[j], end = " ")
#         print()
#         return
#     for i in range(4):
#         # if i == 1: continue
#         alphabet_list[level] = arr[i]
#         abc(level+1)
#
# result = abc(0)
# result

# AAA~DDD까지의 중복순열 중 연속해서 두개의 알파벳이 나오는 경우를 제외하고 출력하기
arr = ['A', 'B', 'C', 'D']
alphabet_list = [0]*3
cnt = [0]*4
def abc(level):
    # if level > 1 and alphabet_list[level-1] == alphabet_list[level-2]: return
    if level == 3:
        for j in range(level):
            print(alphabet_list[j], end = " ")
        print()
        return
    for i in range(4):
        # if level > 0 and (alphabet_list[level-1] == arr[i]): continue
        alphabet_list[level] = arr[i]
        cnt[i] += 1
        abc(level+1)

result = abc(0)
result







































