# import copy
# # 최대공약수를 구하는 유클리드호제법
#
# a, b = map(int, input().split())
# a_copy = copy.deepcopy(a)
# b_copy = copy.deepcopy(b)
#
# answer = 0
# while b:
#     answer = a % b
#     a = b
#     b = answer
# print(a)
#
# # 최대공약수를 통해 최소공배수를 구하기
# # lcm = gcd*(a/gcd)*(b/gcd)
# lcm = (a_copy/a)*(b_copy/a)*a
# print(lcm)
#
# import math


# prime number (소수 구하기)
# 소수 - 1과 자기 자신으로만 나눌 수 있는 수
#
# a=int(input())
# flag=True
# if a>2:
#     for i in range(2,a):
#         if a%i==0:
#             flag=False
#             break
# if flag:print("소수임")
# else: print("소수가 아님")

#에라토스테네스의 체

# a=int(input())
# answer=[]
# check=[True]*(a+1)
# for i in range(2,a+1): #2부터 입력받은 수 까지 모두 확인
#     if check[i]==True: answer.append(i)
#     for j in range(i+i,a+1,i): # 확인하고자 하는 배수에 해당하는 값을 false
#         check[j]=False
# print(*answer)



# a=int(input())
# answer=[]
# check=[True]*(a+1)
# for i in range(2,int(math.sqrt(a))+1): #2부터 입력받은 수의 제곱근 까지 모두 확인
#     if check[i]==False: continue
#     for j in range(i+i,a+1,i): # 확인하고자 하는 배수에 해당하는 값을 false
#         check[j]=False
#
# # 위에 for문이 끝나면.. 소수가 아닌 곳에는 false 체크가 되어 있고
# # 남은 숫자들에는 True 가 남아 있다.
#
# for i in range(2,a+1):
#     if check[i]==True:
#         print(i,end=' ')

# 추가 연습문제
N = int(input())
arr = [list(input()) for _ in range(N)]
b, a = map(int, input().split())

directy = [1, -1, 0, 0]
directx = [0, 0, 1, -1]

# 소화기 소지 유무
A_have = False


def bfs(y0, x0, y1, x1):
    visited = [[0] * N for _ in range(N)]
    queue = [(y0, x0, 0)]
    visited[y0][x0] = 1
    while queue:
        y, x, level = queue.pop(0)

        if y == y1 and x == x1:
            return level

        for i in range(4):
            dx = directx[i] + x
            dy = directy[i] + y
            if 0 <= dx < N and 0 <= dy < N:
                # 소화기를 가지고 있지 않을 땐 불 좌표에 접근 불가
                if A_have == False and visited[dy][dx] == 0:
                    if arr[dy][dx] != '#' and arr[dy][dx] != '$':
                        visited[dy][dx] = 1
                        queue.append([dy, dx, level + 1])
                elif A_have == True and visited[dy][dx] == 0:
                    if arr[dy][dx] != '#':
                        visited[dy][dx] = 1
                        queue.append([dy, dx, level + 1])


# 소화기 좌표와 불 좌표 저장
A_list = []
fire_loc = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'A':
            A_list.append([i, j])
        if arr[i][j] == '$':
            fire_loc = [i, j]

min_cnt = 999
for i in range(len(A_list)):
    cnt1 = bfs(b, a, A_list[i][0], A_list[i][1])
    # 소화기 좌표를 구한 뒤에는 불에 접근 가능하도록 설정
    A_have = True
    cnt2 = bfs(A_list[i][0], A_list[i][1], fire_loc[0], fire_loc[1])
    cnt = cnt1 + cnt2

    if min_cnt > cnt:
        min_cnt = cnt
print(min_cnt)





