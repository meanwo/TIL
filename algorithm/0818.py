# 가장 인기가 많은 사람 구하기 1
# love_line = [[1, 2],
#              [4],
#              [1],
#              [1],
#              [3]]
#
# cnt_list = [0]*5
# for i in range(len(love_line)):
#     for j in range(len(cnt_list)):
#         if j in love_line[i]:
#             cnt_list[j] += 1
# print(cnt_list)
# popular_number = cnt_list.index(max(cnt_list))
#
# popular_name = chr(65+popular_number)
# print(popular_name)
#
# # 가장 인기가 많은 사람 구하기 2
# name=['A','B','C','E','D']
# arr=[ [0,1,1,0,0],
#       [0,0,0,1,0],
#       [0,1,0,0,0],
#       [0,0,0,0,1], # E
#       [0,1,0,0,0]  # D
#       ]
# sum=0
# Max=0
# Maxindex=0
# for j in range(5):
#     sum=0
#     for i in range(5):
#         if arr[i][j]==1:
#             sum+=1
#     if sum>Max:
#         Max=sum
#         Maxindex=j
# print(name[Maxindex])
#

# 문자하나를 입력받고 입력받은 문자의 형제 출력하기
# a = input()
# a_asci = ord(a)-65
#
# arr = [[0, 1, 1, 0, 0, 0],
#        [0, 0, 0, 1, 1, 0],
#        [0, 0, 0, 0, 0, 1],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0]]
#
# bro_index = []
# bro_list = []
# for i in range(5):
#     if arr[i][a_asci] == 1:
#         parent_index = i
#
# for i in range(len(arr[0])):
#     if arr[parent_index][i] == 1:
#         bro_index.append(i)
#
# for i in range(len(bro_index)):
#     bro_list.append(chr(bro_index[i]+65))
#
# bro_list.remove(a)
# print(*bro_list, sep = '')

# #dfs 예제
# name=list(input().split())
# arr = [[0, 1, 1, 0, 0, 0],
#        [0, 0, 0, 1, 1, 0],
#        [0, 0, 0, 0, 0, 1],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0]]
# answer=[]
# def dfs(now):
#     global answer
#     answer.append(name[now])
#     for i in range(6):
#         if arr[now][i]==1:
#             dfs(i)
# #
# dfs(0)  # 0번 인덱스 부터 깊이우선 탐색 시작
# print(*answer)
# name=list(input().split())
# arr = [[0, 1, 1, 0, 0, 0],
#        [0, 0, 0, 1, 1, 0],
#        [0, 0, 0, 0, 0, 1],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0]]
#
# ans = []
#
# def dfs(now):
#     global ans
#     ans.append(name[now])
#     for i in range(len(arr)):
#         if arr[now][i] == 1:
#            dfs(i)
#
# result = dfs(0)
# print(*ans)

# C부터 깊이우선 탐색 시작
arr = [[0, 1, 0, 0],
       [0, 0, 1, 1],
       [1, 0, 0, 1],
       [0, 0, 0, 0]]
name = ['A', 'B', 'C', 'D']
ans =[]
used = [0]*4
# C에 1을 체크하고  dfs 에 들어가기
used[2] = 1

def dfs(now):
    global ans
    ans.append(name[now])
    for i in range(len(arr)):
        if used[i] == 1: continue
        used[i] = 1
        if arr[now][i] == 1:
            dfs(i)

result = dfs(2)
print(*ans)

# A부터 D 까지의 경로 갯수 구하기
# name=list(input().split())  # B A C D
# arr=[
#     [0,0,1,1],
#     [1,0,1,0],
#     [1,0,0,1],
#     [0,0,0,0],
# ]
# used=[0]*4
# cnt=0
# def dfs(now):
#     global cnt
#     if now==3:
#         cnt+=1
#     for i in range(4):
#         if arr[now][i]==1 and used[i]==0:
#             used[i]=1
#             dfs(i)
#             used[i]=0
#
#
# used[1]=1
# dfs(1)
# print(cnt)

# 입력받은 출발점 알파벳 부터 E가 써있는 곳 까지 갈 수 있는 방법이 몇 가지 있는지 출력하기

# arr = [
#     [0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1],
#     [1, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0]
# ]
# used = [0]*5
# # name=list(input().split())  # A B C D E
# name = ['A', 'B', 'C', 'D', 'E']
#
# cnt = 0
# def dfs(now):
#     global cnt
#     if now == 4:
#         cnt += 1
#     for i in range(len(arr)):
#         if arr[now][i] == 1 and used[i] == 0:
#             used[i] = 1
#             dfs(i)
#             used[i] = 0
#
# A = input()
# st_index = 0
# for i in range(5):
#     if name[i]==A:
#         st_index=i
#         break
# used[st_index]=1
# dfs(st_index)
# print(cnt)

# A부터 E까지 최소비용 구하기
# name=['A','B','C','D','E']
# st=input()  # 출발점 입력
# arr = [[0, 4, 0, 0, 0],
#        [0, 0, 1, 2, 9],
#        [5, 0, 0, 7, 0],
#        [0, 0, 0, 0, 1],
#        [0, 0, 0, 0, 0]]
#
# used_list= [0]*5
# min = 999
#
# def dfs(now, sum):
#     global min
#     if now == 4:
#         if sum < min:
#             min = sum
#
#     for i in range(len(arr)):
#         if arr[now][i] != 0 and used_list[i] == 0:
#             used_list[i] = 1
#             dfs(i, sum+arr[now][i])
#             used_list[i] = 0
#
# st_index = 0
# for i in range(5):
#     if name[i] == st:
#         st_index = i
#         break
#
# used_list[st_index] = 1
# result = dfs(st_index, 0)
#
# print(min)
















