# deque 예제
# from collections import deque
# q=deque()
# q.append(2)
# q.append(3)
# q.append(4)
# q.append(5)
# print(*q)
# q.appendleft(9)
# print(*q)
# x=q.popleft()
# print(x)
# print(*q)


# from collections import deque
# name=list(input().split())
# arr=[
#     [0,1,0,1,0,0],
#     [0,0,1,0,1,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,1],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
# ]
# answer=[]
# def bfs(st):
#     global answer
#     q=deque()
#     q.append(st)
#     while q:
#         now=q.popleft()
#         answer.append(name[now])
#         for i in range(6):
#             if arr[now][i]==1:
#                 q.append(i)
#
# bfs(0)
# print(*answer)

# from collections import deque
# name=list(input().split()) #A B C D
# arr=[
#     [0,1,1,0],
#     [0,0,1,1],
#     [0,1,0,1],
#     [0,0,0,0],
# ]
# used=[0]*4
# answer=[]
# def bfs(st):
#     global answer
#     q=deque()
#     q.append(st)
#     while q:
#         now=q.popleft()
#         answer.append(name[now])
#         for i in range(4):
#             if arr[now][i]==1:
#                 if used[i]==0:
#                     used[i]=1
#                     q.append(i)
#
# used[1]=1 # 시작 index에 1체크
# bfs(1) # 시작 index 적고 시작
# print(*answer)


# flood 문제를 bfs로 풀이 (개화시기)
# from collections import deque
# n = int(input())
# y, x = map(int, input().split())
# arr = [[0]*n for _ in range(n)]
# arr[y][x] = 1
# q = deque()
# q.append([y, x])
#
# while q:
#     now = q.popleft()
#     y, x = now[0], now[1]
#     directy = [-1, 1, 0, 0]
#     directx = [0, 0, -1, 1]
#     for i in range(4):
#         dy = y+directy[i]
#         dx = x+directx[i]
#         if 0 <= dy < n and 0 <= dx < n:
#             if arr[dy][dx] == 0:
#                 arr[dy][dx] = arr[y][x] + 1
#                 q.append([dy,dx])
# for i in arr:
#     print(*i)
# 특정 좌표 y,x에 초깃값을 주고 0,0 에 언제 꽃이 피는지 확인.

# from collections import deque
# n = int(input()) # map 사이즈 입력
# y, x = map(int,input().split()) # 시작점 입력
# arr = [[0]*n for _ in range(n)]
#
# arr[y][x] = 1
# q = deque()
# q.append((y, x, 0))
#
# answer=0
# while q:
#     y,x,level=q.popleft()
#     # if y==0 and x==0: answer=level
#     directy=[0,0,1,-1]
#     directx=[1,-1,0,0]
#     for i in range(4):
#         dy=y+directy[i]
#         dx=x+directx[i]
#         if 0<=dy<n and 0<=dx<n:
#             if arr[dy][dx]==0:
#                 arr[dy][dx]=arr[y][x]+1
#                 q.append((dy,dx,level+1))
#                 if dy==0 and dx==0:
#                     answer=level+1
# for i in arr:
#     print(*i)
# print(answer)

from collections import deque

n = int(input())
loc = list(map(int, input().split()))

arr = [[0]*n for _ in range(n)]
arr[loc[0]][loc[1]] = 1
arr[loc[2]][loc[3]] = 1

q = deque()
q.append((loc[0],loc[1], 0))
q.append((loc[2],loc[3], 0))
answer=0
while q:
    flag = 1
    for  i in range(n):
        for j in range(n):
            flag *= arr[i][j]
    if flag != 0:
        answer = level+1
        break

    y,x,level=q.popleft()
    # if y==0 and x==0: answer=level
    directy=[0,0,1,-1]
    directx=[1,-1,0,0]
    for i in range(4):
        dy=y+directy[i]
        dx=x+directx[i]
        if 0<=dy<n and 0<=dx<n:
            if arr[dy][dx]==0:
                arr[dy][dx]=arr[y][x]+1
                q.append((dy,dx,level+1))
                # if dy==0 and dx==0:
                #     answer=level+1

print(answer)


















