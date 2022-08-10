# 간결하게 부분집합을 생성하는 방법
# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr)
#
# for i in range(1<<n):   # 1<<n : 부분 집합의 개수
#     for j in range(n):  # 원소의 수만큼 비트를 비교함
#         if i & (1<<j):  # i의 j번 비트가 1인경우
#             print(arr[j], end=",")   #j번 원소 출력
#     print()   # 개행
# print()

# 이진 검색 알고리즘
# def binarySearch(a, N, key):
#     start = 0
#     end = N-1
#     while start <= end:
#         middle = (start+end)//2
#         if a[middle] == key:
#             return True
#         elif a[middle] > key:
#             end = middle - 1
#         else:
#             start = middle + 1
#     return False  #못 찾고 반복문이 종료되는 경우

# sys.stdin 통해 입력 받아오기 예제
# import sys
# sys.stdin = open("input.txt", "r")
#
#
# # 1.문자열 입력 받기
# # st = 'hello'
# st = input()
# print(st)
#
#
# # 2.정수형 변수 입력 받기
# # N = 45
# # A, B, C = 1, 2, 3
#
# N = int(input())
# print(N)
#
# A, B, C = map(int, input().split())
# print(A, B, C)
#
# # 3.실수형 변수 입력 받기
# # F = 3.14
# # A, B, C = 1.2, 2.3, 3.4
#
# F = float(input())
# print(F)
# A, B, C = map(float, input().split())
# print(A, B, C)
#
# # 4.한 줄에 있는 공백으로 구분된 단어들을 각각 문자열로 리스트에 저장하기
# # lst = ['one', 'two', 'three']
# lst = list((input().split()))
# print(lst)
#
#
# # 5.한 줄에 있는 공백으로 구분된 숫자들을 각각 숫자로 리스트에 저장하기
# # lst = [1, 2, 45, 43]
# lst = list(map(int, input().split()))
# print(lst)
#
# # 6.한 줄에 있는 공백없는 한자리 숫자들을 각각 숫자로 리스트에 저장하기
# # lst = [1, 2, 3, 4]
# lst = list(map(int, input()))
# print(lst)
#
# # 7.2차원 (N*N) 공백없는 한자리 숫자들을 2차원 arr에 저장
# # 4
# # 1011
# # 1001
# # 0001
# # 1000
#
# N = int(input())
# arr_input = [list(map(int, input())) for _ in range (N)]
# print(arr_input)
#
#
# # 8.2차원 (N*N) 정수값을 2차원 arr에 저장 (N값과 arr값)
# # 4
# # 1 2 3 4
# # 5 6 7 8
# # 9 10 11 12
# # 13 14 15 16
#
# N = int(input())
# arr_input = [list(map(int, input().split())) for _ in range (N)]
# print(arr_input)
#
#
# # 9.(입력은 아니지만) 0값 10개를 가진 1차원 lst 생성
# # lst = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# lst = [0]*10
# print(lst)
# # 10.(입력은 아니지만) 0값 3 * 3 개를 가진 2차원 arr생성
# # arr = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
#
# arr = [[0]*3 for _ in range(3)]
# print(arr)

# 좌표 기준으로 상하좌우 값의 합 출력
# A = [[2, 7, 3], [8, 5, 9], [7, 4, 6]]
#
# def sum_around(a, b):
#     sum_A = 0
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]
#     for i in range(len(dx)):
#         sum_A += A[a+dx[i]][b+dy[i]]
#
#     return sum_A
#
# result = sum_around(1,1)
# print(result)

# 디버깅 예제
# def abc(y,x):
#     x=y+1
#     z=y+x
#     return z
# a=10
# b=10
# b=20
# c=30
# c=40
# c=50
# ret=abc(a,b)
#
# print(ret)

# 좌표 기준으로 5방향 합의 max값 출력
# A = [[3, 5, 4], [1, 1, 2], [1, 3, 9]]
#
# def sum_around():
#
#     Max_index = [0, 0]
#     Max_sum = 0
#     dx = [0, 0, -1, 1, 0]
#     dy = [1, -1, 0, 0, 0]
#     for a in range(3):
#         for b in range(3):
#             sum_A = 0
#             for i in range(len(dx)):
#                 if a+dx[i] >= 0 and b+dy[i] >= 0 and a+dx[i] <= 2 and b+dy[i] <= 2:
#                     sum_A += A[a+dx[i]][b+dy[i]]
#
#             if Max_sum < sum_A:
#                 Max_sum = sum_A
#                 Max_index = [a, b]
#     return Max_sum, Max_index
#
# result = sum_around()
# print(result)

# 2x3 밭의 최대 값 구하기
# n, m = map(int, input().split())
# A = [list(map(int, input().split())) for _ in range(3)]
#
# def getsum():
#     max_A = 0
#     max_index = [0, 0]
#     for g in range(2):
#         for h in range(3):
#             sum_A = 0
#             for j in range(2):
#                 for k in range(3):
#                     sum_A += A[j+g][k+h]
#                     if max_A < sum_A:
#                         max_A = sum_A
#                         max_index = g, h
#     return max_A, max_index
#
# result = getsum()
# print(result[0])
# print(result[1])

