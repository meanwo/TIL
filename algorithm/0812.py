# def show_num(n):
#     print(n)
#     if n ==1:
#         print(n)
#         return
#     show_num(n-1)
#     print(n)
#
# result = show_num(6)
#
# def show_odd(n):
#     print(n)
#     if n == 9:
#         return
#     show_odd(n+2)
#     print(n)
#
# result2 = show_odd(1)


# 재귀 연습
# def abc(level):
#     # print('#', end='')
#     if level == 2:
#         # print('#', end='')
#         return
#     # print('#', end='')
#     for i in range(2):
#         # print('#', end='')
#         abc(level+1)
#         print(level, end='')
#     # print(level, end='')
# abc(0)

#연속된 구간의 합의 최대를 구하세요.

# n = int(input())
# A = [4, 7, 1, 8, 9, 3, 5, 8, 6, 6, 9]
#1
# for i in range(len(n)):

# for i in range(len(A)-n+1):
#     sum_max = 0
#     for j in range(n):
#         sum_max += A[i+j]
# print(sum_max)

#2
# sum = 29
# max_sum = 0
# for i in range(len(A)-n):
#     sum+= (-1)*A[i]+A[i+n]
#     if max_sum < sum:
#         max_sum = sum
# print(max_sum)

#연속된 숫자들의 합이 target이 되는 경우는?
# 투포인터 알고리즘
# n,target=map(int,input().split())
# arr=list(map(int,input().split()))
#
# cnt,sum=0,0
# high,low=0,0
# while(1):
#     if sum>target:        # 합이 타겟보다 크면.. (범위를 줄여야 하니까)
#         sum-=arr[low]       # sum에서 뺴고
#         low+=1              # low 의 index를 1증가
#     elif high==n: break
#     else:
#         sum+=arr[high]      # 합이 타겟보다 작거나 같다면
#         high+=1             # sum에 더하고 high의 인덱스를 1증가
#     if sum==target:
#         cnt+=1
# print(cnt)

#1
A = [[4, 7, 1, 8], [5, 5, 9, 2], [5, 9, 5, 9], [1, 2, 9, 7]]
#
# sum_around = 0
# max_sum = 0
# max_index = [0, 0]
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]
#
# for i in range(4):
#     for j in range(4):
#         sum_around = 0
#         for k in range(4):
#             if i+dy[k] >= 0 and i+dy[k] <= 3 and j+dx[k] >= 0 and j+dx[k] <= 3:
#                 sum_around += A[i+dy[k]][j+dx[k]]
#                 if sum_around > max_sum:
#                     max_sum = sum_around
#                     max_index = (i, j)
#
# print(max_sum, max_index)

# 2

sum_diagonal = [0]*(2*len(A)-1)

# for i in range(2*len(A)-1):
for i in range(4):
    for j in range(4):
        for k in range(-3, 4):
            if i-j == k:
                sum_diagonal[k+3] += A[i][j]

# 우상단 부터 시작
print(sum_diagonal)

#3
sum_upper = 0
sum_lower = 0
for i in range(4):
    for j in range(4):
        if i > j:
            sum_lower += A[i][j]
        elif i < j:
            sum_upper += A[i][j]

print(sum_upper, sum_lower)