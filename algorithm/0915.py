# 정점의 개수 5
# 간선의 개수 8

# 정점 V 연결을 위한 최소 간선 횟수 E = V-1

# 크루스칼 알고리즘 핵심
# 비용 기준으로 오름차순 정렬.
# 사이클이 발생하지 않도록(최소 연결을 구현하기 위해) union, find 활용
# E= V-1 일 때 연산 종료

# V = int(input())
# E = int(input())
# arr=[0]*200
# info_list = []
# for i in range(E):
#     a, b, cost = input().split()
#     cost = int(cost)
#     info_list.append([a, b, cost])
# sort_list = sorted(info_list, key=lambda x: x[2])
#
# def findboss(member):
#     global arr
#     if arr[ord(member)] == 0:
#         return member
#     ret = findboss(arr[ord(member)])
#     # 최상위 부모를 찾을 때 계산 과정을 줄여주는 부분
#     arr[ord(member)]=ret
#     return ret
#
# # union 함수
# def union(a,b):
#     global arr
#
#     fa,fb=findboss(a), findboss(b)
#     if fa == fb:return 1
#     arr[ord(fb)]=fa
#
# sum_cost = 0
# cnt = 0
#
# # 최소 비용 구하는 함수
# def minumum_cost(E):
#     global sort_list, sum_cost, cnt
#     for i in range(E):
#         if cnt == V-1:
#             break
#         a, b = sort_list[i][0], sort_list[i][1]
#         ret = union(a, b)
#         if ret == 1:
#             continue
#         sum_cost += sort_list[i][2]
#         cnt += 1
#
# result = minumum_cost(E)
# print(sum_cost)


# 각 항에서 1~4 사이의 숫자를 1개씩 택해서 다
# 더했을떄 10이 나오는 경우는 몇가지 인가요?
# n 개의 항에서 1~4 사이의 숫자를 택할 것입니다.

# cnt=0
# def abc(level,sum):
#     global n,cnt
#     if level==n:
#         if sum==10:
#             cnt+=1
#         return
#     for i in range(1,5):
#         abc(level+1,sum+i)
#
# n=int(input())
# abc(0,0) #level sum
# print(cnt)

# 4명이 놀이동산에 갔습니다. [M B T I]
# 놀이기구를 타는데 1 unit에 3명이 앉을 수 있습니다.
# 4명중에 1명이 고소공포증이 있어서 놀이기구를 안탄다고 합니다.
# 놀이기구를 탈 조합을 모두 출력해 주세요.

# name='MBTI'
# path=['']*3
#
# def abc(level,start):
#     if level==3:
#         for i in range(3):
#             print(path[i],end=' ')
#         print()
#         return
#     for i in range(start,4):
#         path[level]=name[i]
#         abc(level+1,i+1)
#         path[level]=0
#
# abc(0,0)


# 두 라인에서 숫자를 1개씩 번갈아 가며 선택을
# 하고자 합니다.
# 첫번째 라인에서 숫자를 1개 택한 후 *1을 하고
# 두번째 라인에서 숫자를 1개 택한 후 *2를 하고
# 첫번쨰 라인에서 숫자를 1개 택한 후 *3을 하고..
# 두번째 라인에서 숫자를 1개 택한 수 *4를 하는등
# 가중치가 1씩 증가되는 값으로 뽑은 숫자에 곱해 줍니다.
#
# 가중치를 곱한 후 모두 더했을때
# 합이 0에 가장 가까운 수를 구하고자 합니다.
# 이때 총 합은 몇일까요?
# (각 라인의 숫자는 1번씩만 사용하여 모든 숫자를 한번씩 뽑습니다.)
# line1 = [3, 7, 1, -3, -6, 1]
# line2 = [7, -4, 1, -5, 3, 2]
#
# used_list1 = [0]*6
# used_list2 = [0]*6
# min_total = 9999
# def dfs(level, total):
#
#     global min_total, answer
#     if level == 12:
#         if abs(total) < min_total:
#             min_total = abs(total)
#             answer = total
#         return
#     if level % 2 == 0:
#         for i in range(6):
#             if used_list1[i] == 0:
#                 used_list1[i] = 1
#                 dfs(level+1, total+line1[i]*(level+1))
#                 used_list1[i] = 0
#     else:
#         for i in range(6):
#             if used_list2[i] == 0:
#                 used_list2[i] = 1
#                 dfs(level+1, total+line2[i]*(level+1))
#                 used_list2[i] = 0
# dfs(0,0)
# print(answer)



# power=[50,40,99,5,25,6,37]
#            a  ,b ,c  ,d, e ,f, g

# 서바이벌 게임
# a ~ g 를 두팀으로 나누어서
# 게임을 하고자 합니다.
# 두 팀으로 나누었을때
# 두 팀의 전투력 차이가 최소가 되었을때
# 최소 전투력 차이는 몇일까요?
# 모든 선수는 경기에 참가를 하며
# 1인팀도 가능 합니다.

# power=[50,40,99,5,25,6,37]
# check=[0]*7
# Min=21e8
#
# def dfs(start,level,sum):
#     global Min,power
#     against=0
#     for i in range(7):
#         if check[i]==0:
#             against+=power[i]
#     gap=abs(sum-against)
#     Min=min(Min,gap)
#
#     if level==6:
#         return
#     for i in range(start,7):
#         check[i]=1
#         dfs(i+1,level+1,sum+power[i])
#         check[i]=0
# dfs(0,0,0) # start,level,sum
# print(Min)

# [7 3 5 4]
# 각각의 숫자에
# 2를 곱하거나 또는
# 3으로 나누거나 또는
# 5를 더해서 숫자를 바꾼 후
#
# 바뀐 4개의 숫자들의 곱을 구한 후
# 그 곱의 Max값을 출력해 주세요.
#
# (추가설명)
# 7 3 5 4 가 있다면
# 7에 2를 곱하거나 3으로 나누거나 5을 더한 값으로 바꿈
# 3에 2를 곱하거나 3으로 나누거나 5을 더한 값으로 바꿈
# 5에 2를 곱하거나 3으로 나누거나 5을 더한 값으로 바꿈
# 4에 2를 곱하거나 3으로 나누거나 5을 더한 값으로 바꿈
#
# 바뀐 숫자들을 모두 곱했을때 MAX 값 출력하기

# n = int(input())
# arr = list(map(int, input().split()))
# max = 0
# def dfs(level, total):
#     global max
#     if level == n:
#         if max < total:
#             max = total
#         # print(max)
#         return
#     for i in range(3):
#         if i == 0:
#             dfs(level+1, total*arr[level]*2)
#         elif i == 1:
#             dfs(level+1, total*(arr[level]//3))
#         elif i == 2:
#             dfs(level+1, total*(arr[level]+5))
#
# dfs(0, 1)
# print(max)


# gop을 전역으로 선언 후
# 원상복구를 할때

# n=4
# arr=[7,3,5,4]
# Max=-21e8
#
# def dfs(level):
#
#     global  Max
#
#     if level==4:
#         gop=1
#         for i in range(4):
#             gop*=arr[i]
#             Max=max(Max,gop)
#         return
#
#     backup=arr[level]
#
#     arr[level]*=2
#     dfs(level+1)
#     arr[level]=backup     # 원상복구
#
#     arr[level]/=3
#     dfs(level+1)
#     arr[level]=backup    # 원상복구 arr[level]*=3 (X)
#
#     arr[level]+=5
#     dfs(level+1)
#     arr[level]=backup   # 원상복구
#
# dfs(0)
# print(Max)

# 땅파기 문제
# 땅을 개척작업을 통해
# 가치를 올리고자 합니다.
# (위아래좌우그리고 자기자신의 가치가 *7한수 %10한 값으로 바뀜)
#
# 총 3곳을 개발할 예정..
# 중복가능( 한번 개발한 했던곳을 또 개발 가능)
# 개발후 3*3배열의 땅의가치가 MAx가 되었을때
# 그 MAx값을 출력해 주시면 됩니다.
# import copy
#
# arr = [[4, 2, 1], [5, 3, 9], [7, 8, 1]]
# dx = [0, 0, 0, 1, -1]
# dy = [0, 1, -1, 0, 0]
#
# max_sum = 0
# def dfs(level):
#     global max_sum, arr
#     backup = copy.deepcopy(arr)
#     if level == 3:
#         sum_arr = 0
#         for i in range(3):
#             for j in range(3):
#                 sum_arr += arr[i][j]
#         if max_sum < sum_arr:
#             max_sum = sum_arr
#         return
#     for j in range(3):
#         for k in range(3):
#
#             for i in range(5):
#                 if 0 <= j+dy[i] <= 2 and 0 <= k+dx[i] <= 2:
#
#                     arr[j+dy[i]][k+dx[i]] = (arr[j+dy[i]][k+dx[i]]*7)%10
#
#             dfs(level+1)
#             arr = copy.deepcopy(backup)
# dfs(0)
# print(max_sum)

