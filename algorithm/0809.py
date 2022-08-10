
# # 내장함수 쓰지 않고 max 값 구현
# a = [21,6,21,4,7]
# max_a = a[0]
# for i in range(len(a)-1):
#     if a[i] > max_a:
#         max_a = a[i]
# print(max_a)
#
# #리스트 안 값들의 합 구하기
# a_sum = 0
# for num in a:
#     a_sum += num
# print(a_sum)
#
# #리스트 안에 최대값과 그 최대값의 등장횟수 구하기
#
# count_max = 0
# for i in range(len(a)-1):
#     if a[i] > max_a:
#         max_a = a[i]
#
# for num in a:
#     if num == max_a:
#         count_max += 1
# print(max_a, count_max)


# # 선택정렬 구현
#
# A = [4, 7, 1, 3, 5, 2]
# for i in range(len(A)-1):
#     for j in range(i+1, len(A)):
#         if A[j] < A[i]:
#             A[i], A[j] = A[j], A[i]
#
# print(A)


#삽입정렬

# A = [4, 7, 1, 3, 5, 2]
# result = []
# for i in range(6):
#     result.append(A[i])
#     for j in range(i, 0, -1):
#         if result[j] < result[j-1]:
#             result[j], result[j-1] = result[j-1], result[j]
#         else:
#             break
# print(result)

#버블정렬
# A = [8, 3, 12, 10, 1]
# for i in range(len(A)-1):
#     for j in range(len(A)-1-i):
#         if A[j] >  A[j+1]:
#             A[j], A[j+1] = A[j+1], A[j]
# print(A)

# Direct Addressing Table
# 1 기존방법
# A = [4, 7, 1, 3, 4, 1, 2, 4]
# B = list(map(int, input().split()))
#
# B_count = [0]*len(B)
#
# for i in range(len(B)):
#     for j in range(len(A)):
#         if B[i] == A[j]:
#             B_count[i] +=1
#     print('{}는 {}개'.format(B[i], B_count[i]))

# 2 Direct Addressing Table
# bucket을 만들고 bucket에 해당하는 인덱스만 출력하는 방식
# A = [4, 7, 1, 3, 4, 1, 2, 4]
# B = list(map(int, input().split()))
#
# A_bucket = [0]*10
#
# for i in range(len(A)):
#     A_bucket[A[i]] += 1
#
# print(A_bucket)
# for i in range(len(B)):
#     print('{}는 {}개'.format(B[i], A_bucket[B[i]]))

# n개의 정수를 입력받고 어떤 수가 몇 개 입력되었는지 출력하라.
# n = int(input())
# A = list(map(int, input().split()))
#
# A_bucket = [0]*101
#
# for i in range(len(A)):
#     A_bucket[A[i]] += 1
#
# for i in range(len(A_bucket)):
#     if A_bucket[i] > 0:
#         print('{}는 {}개'.format(i, A_bucket[i]))

# ## counting 정렬
# n = int(input())
# A = list(map(int, input().split()))
#
# # dat 등록
# A_bucket = [0]*101
# for i in range(n):
#     A_bucket[A[i]] += 1
#
# # 누적합 구하기
# for i in range(1, len(A_bucket)):
#     A_bucket[i] += A_bucket[i-1]
#
# print(A_bucket)
# # 값 넣기
# result = [0]*101
# for i in range(n):
#     index = A[i]
#     result[A_bucket[index]-1] = A[i]
#     A_bucket[index] -= 1
#
# # print(result)
# for i in range(n):
#     print(result[i], end = ' ')

#거스름돈 만들기 while문
# coin = [100, 50, 10]
# change = int(input())
# answer = 0
# index = 0
# while True:
#     cnt = change//coin[index]
#     change -= (cnt*coin[index])
#     answer += cnt
#     index += 1
#     if index == 3:
#         break
# print(answer)

#거스름돈 만들기 for문
# coin = [100, 50, 10]
# change = int(input())
# cnt = 0
# for i in range(len(coin)):
#     cnt += change//coin[i]
#     change = change % coin[i]
# print(cnt)

# 패턴찾기
# arr=[3,6,5,8,5,3,5,8,5,3,3,1,1,3]
# pattern=[3,5,8,4]
# flag = 0
# def isPattern(index):
#     for i in range(4):
#         if arr[index+i] != pattern[i]:
#             # 중요!! if의 조건을 만족하면 반복문을 더 돌지 않고 0을 return
#             return 0
#     return 1
#
# for i in range(11):
#     ret = isPattern(i)
#     if ret == 1:
#         flag = 1
#         break
#
# if flag:
#     print("패턴존재")
# else:
#     print("존재하지 않음")



#패턴찾기2
board = [
    ["A", "B", "G", "K"],
    ["T", "T", "A", "B"],
    ["A", "C", "T", "T"]
]

ptn = [list(input()) for _ in range(2)]
cnt = 0
def isPattern(row, col):
    for i in range(2):
        for j in range(2):
            if board[row+i][col+j] != ptn[i][j]:
                return 0
    return 1

for i in range(2):
    for j in range(3):
        if isPattern(i, j):
            cnt +=1
if not cnt:
    print("존재하지 않음")
else:
    print("패턴존재")


