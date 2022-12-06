# 1.path 배열안에 문자를 비교하면서 조합을 출력하는 방법
# arr=['a','b','c','d']
# path=['']*3
#
#
# def abc(level):
#     if level==3:
#         for i in range(3):
#             print(path[i],end='')
#         print()
#         return
#
#     for i in range(4):
#         #1 path[level-1] -> 그전 단계에서 타고 들어온 곳
#         #2 arr[i] -> 앞으로 들어갈 가지
#         #3 그전 들어온 가지 < 앞으로 들어갈 가지  (True)
#         if level>0 and path[level-1] >= arr[i]: continue
#         path[level]=arr[i]
#         abc(level+1)
#
# abc(0)


# 2. for문의 i값의 변화를 이용한 조합 출력하기
# arr=['a','b','c','d']
# path=['']*3
#
#
# def abc(level, start):
#     if level==3:
#         for i in range(3):
#             print(path[i],end='')
#         print()
#         return
#
#     for i in range(start, 4):
#         path[level] = arr[i]
#         abc(level+1, i+1)
#
# abc(0,0)

# n개의 주사위를 던져서 나올 수 있는 모든 숫자를 출력

# 1. 중복순열
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
# result = abc(0, dice_list)


# 2. 순열
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
#
#         if used[j] == 1: continue
#         dice_list[level] = dice[j]
#         used[j] = 1
#         abc(level+1)
#         used[j] = 0
#         # dice_list[level] =0
#
# result = abc(0)

# 3. 조합
# n = int(input())
# dice = [1, 2, 3, 4, 5, 6]
# dice_list = [0]*n
#
# def abc(level):
#     if level == 3:
#         for i in range(3):
#             print(dice_list[i], end='')
#         print()
#         return
#
#     for i in range(6):
#         #1 path[level-1] -> 그전 단계에서 타고 들어온 곳
#         #2 arr[i] -> 앞으로 들어갈 가지
#         #3 그전 들어온 가지 < 앞으로 들어갈 가지  (True)
#         if level > 0 and dice_list[level-1] >= dice[i] : continue
#         dice_list[level] = dice[i]
#         abc(level+1)
# abc(0)

# 4. 중복조합
# n = int(input())
# dice = [1, 2, 3, 4, 5, 6]
# dice_list = [0]*n
#
# def abc(level):
#     if level == 3:
#         for i in range(3):
#             print(dice_list[i], end='')
#         print()
#         return
#
#     for i in range(6):
#         #1 path[level-1] -> 그전 단계에서 타고 들어온 곳
#         #2 arr[i] -> 앞으로 들어갈 가지
#         #3 그전 들어온 가지 < 앞으로 들어갈 가지  (True)
#         if level > 0 and dice_list[level-1] > dice[i] : continue
#         dice_list[level] = dice[i]
#         abc(level+1)
# abc(0)

# 4. 중복조합 (for 문의 i값 이용)
# n = int(input())
# dice = [1, 2, 3, 4, 5, 6]
# dice_list = [0]*n
# cnt_list = [0]*6
# is_duple = []
# def abc(level, start):
#     if level == 3:
#         for i in range(3):
#             print(dice_list[i], end='')
#         print()
#         return
#
#     for i in range(start, 6):
#         dice_list[level] = dice[i]
#         abc(level+1, i)
# abc(0, 0)

a=['a','n','t','i','c']
b=['a','b']
c = list(set(a+b))
print(c)
