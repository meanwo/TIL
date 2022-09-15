# 1번
# arr= [0]*200
# n = int(input())
# edge = []
# for i in range(n):
#     edge.append(input().split())
#
# def findboss(member):
#     if arr[ord(member)] == 0:
#         return member
#     ret = findboss(arr[ord(member)])
#     arr[ord(member)] = ret
#     return ret
#
# def union(a, b):
#     fa, fb = findboss(a), findboss(b)
#     if fa == fb:
#         return 1
#     arr[ord(fb)] = fa
#
# answer = 0
# for i in range(n):
#     a, b = edge[i]
#     ret = union(a, b)
#     if ret == 1:
#         answer = 1
#         break
# if answer:
#     print('발견')
# else:
#     print('미발견')


# 2번
# group = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H'], ['I', 'J']]
# arr = [0]*200
#
# def findboss(member):
#     if arr[ord(member)] == 0:
#         return member
#     ret = findboss(arr[ord(member)])
#     arr[ord(member)] = ret
#     return ret
#
# def union(a, b):
#     fa, fb = findboss(a), findboss(b)
#     if fa == fb:
#         return 1
#     arr[ord(fb)] = fa
#
#
# print(arr)
#
# n = int(input())
# for i in range(n):
#     x, y = input().split()
#     union(x, y)
#
# for i in range(4):
#     for j in range(1, len(group[i])):
#         union(group[i][0], group[i][j])
#
# result = len(set(arr))-1
#
# print(f'%d개' %result)

# 3번
# arr = [0]*200
#
# def findboss(member):
#     if arr[member] == 0:
#         return member
#     ret = findboss(arr[member])
#     arr[member] = ret
#     return ret
#
# def union(a, b):
#     fa, fb = findboss(a), findboss(b)
#     if fa == fb:
#         return 1
#     arr[(fb)] = fa
#
# n = int(input())
# group = [list(map(int, (input().split()))) for _ in range (n)]
# # print(group)
#
# group_list = []
# for i in range(n):
#     for j in range(i+1):
#         if group[i][j] == 1:
#             group_list.append([i, j])
#
# # print(group_list)
# answer = 0
# for i in range(len(group_list)):
#     ret = union(group_list[i][0], group_list[i][1])
#     if ret == 1:
#         answer = 1
#         break
# if answer:print("cycle 발견")
# else: print("미발견")

# 4번
arr = [0]*200
N, K = map(int, input().split())
info_list = []
for i in range(N):
    info_list.append(input().split())

for i in range(N):
    if info_list[i][0].isalpha():
        arr[int(info_list[i][1])] = info_list[i][0]
    elif info_list[i][1].isalpha():
        arr[int(info_list[i][0])] = info_list[i][1]
    elif arr[int(info_list[i][0])] != 0:
        arr[int(info_list[i][1])] = arr[int(info_list[i][0])]
    elif arr[int(info_list[i][1])] != 0:
        arr[int(info_list[i][0])] = arr[int(info_list[i][1])]

for i in range(N):
    if info_list[i][0].isalpha():
        arr[int(info_list[i][1])] = info_list[i][0]
    elif info_list[i][1].isalpha():
        arr[int(info_list[i][0])] = info_list[i][1]
    elif arr[int(info_list[i][0])] != 0:
        arr[int(info_list[i][1])] = arr[int(info_list[i][0])]
    elif arr[int(info_list[i][1])] != 0:
        arr[int(info_list[i][0])] = arr[int(info_list[i][1])]

print(arr)
for i in range(len(arr)):
    if arr[i] != 0:
        print(arr[i], end= '')

# 5번

arr = [0]*200
n = int(input())
num_list = list(map(int, input().split()))
command_cnt = int(input())
# print(num_list)

def findboss(member):
    if arr[ord(member)] == 0:
        return member
    ret = findboss(arr[ord(member)])
    arr[ord(member)] = ret
    return ret

def union(a, b):
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return 1
    arr[ord(fb)] = fa

for i in range(command_cnt):
    command = list(input().split())
    if command[0] == 'alliance':
        a, b = command[1], command[2]
        union(a, b)
print(arr)
