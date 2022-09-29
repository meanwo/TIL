
# 두 단어가 애너그램인지 판별하는 문제
# 나의 풀이
# word1 = list(input())
# word2 = list(input())
# for i in range(len(word1)):
#     if word1[0] in word2:
#         target = word1[0]
#         word1.remove(target)
#         word2.remove(target)
#
# if len(word1) == 0 and len(word2) == 0:
#     print('it is anagram')
# else:
#     print('it is not anagram')
#===============================================

# dat 이용하는 방식
# arr1=input()
# arr2=input()
# board1=[0]*26
# board2=[0]*26
# for i in (arr1):
#     board1[ord(i)-ord('a')]+=1
# for i in (arr2):
#     board2[ord(i) - ord('a')] += 1
# flag=1
# for i in range(26):
#     if board1[i]!=board2[i]:
#         flag=0
#         break
# if flag: print('anagram')
# else: print('not anagram')

#===============================================
# sort 사용하는 방식
# vect1=input()
# vect2=input()
# if sorted(vect1)==sorted(vect2):
#     print('아나그램')
# else: print('아나그램 아님')


# 가장 긴 애너그램을 만들기 위해 몇 개의 문자를 제거해야 하는지
# 나의 풀이
# word1 = list(input())
# word2 = list(input())
#
# cnt = 0
# word1_dict = {}
# anagram_list = []
# for i in range(len(word1)):
#     if word1[i] not in word1_dict:
#         word1_dict[word1[i]] = 1
#     else:
#         word1_dict[word1[i]] += 1
#
# for i in range(len(word2)):
#     if word2[i] in word1_dict and word1_dict[word2[i]] != 0:
#         word1_dict[word2[i]] -= 1
#         anagram_list.append(word2[i])
#
# print(len(word1)- len(anagram_list) + len(word2) - len(anagram_list))

# dat 이용
# a='ggbbc'
# b='aabbkk'
#
# dat=[0]*26
# for i in a:
#     dat[ord(i)-ord('a')]+=1
#
# for i in b:
#     dat[ord(i)-ord('a')]-=1
#
# cnt=0
# for i in range(26):
#     if dat[i]!=0:
#         cnt+=abs(dat[i])
#
# print(cnt)

# word2의 부분 문자열에서 word1의 애너그램이 되는 경우의 수 구하기
# word1 = input()
# word2 = input()
# cnt = 0
# for i in range(len(word2)-len(word1)+1):
#     if sorted(word2[i:i+len(word1)]) == sorted(word1):
#         cnt += 1
# print(cnt)


# 딕셔너리 복습
dict1={}
dict2=dict()

burger={'cy':3000,'wp':5000}

# 싸이버거 가격만 출력!


# burger={
#     'mst':{'cy':3000,'chips':500},
#     'mc':{'bm':5000,'chips':700}
# }

# 빅맥 가격만 출력!

#맘스터치 칩스 가격 1000원 인상


# 딕셔너리 mst 값 삭제


# =============================================
#연습문제

#딕셔너리 값 출력하기
# burger={
#     'mst':{'cy':3000,'chips':500},
#     'mc':{'bm':5000,'chips':700}
# }
# for i in burger.values():
#     print(i,end=' ')
# print(burger['mst']['cy'])
# print(burger['mc']['bm'])

# burger['mc']['chips'] += 1000
# print(burger)
#
# # 삭제하기
# del burger['mst']
#
# print(burger)
# 출력결과 1
# mst bm

# 출력결과 2
# {'cy':3000,'chips':500}
# {'bm':5000,'chips':700}

# 출력결과 3
# 3000
# 500
# 5000
# 700


# 출력결과 4
# mst {'cy': 3000, 'chips': 500}
# mc {'bm': 5000, 'chips': 700}


# 출력결과 5
# cy 3000
# chips 500
# bm 5000
# chips 700

# =============================================

# 정렬 후 출력하기

# mst={'cy':3000,'chips':500,'coke':300}
#
#
# print(dict(sorted(mst.items(), key = lambda x:x[1])))

# 가격 오름차순 으로 정렬 후 출력하기
# 출력결과
# coke 300
# chips 500
# cy 3000


# 가격 내림차순 으로 정렬 후 출력하기
#출력결과
# cy 3000
# chips 500
# coke 300


# 이름 기준으로 오름차순
# 출력결과
# chips 500
# coke 300
# cy 3000


# 이름 기준으로 내림차순
# 출력결과
# cy 3000
# coke 300
# chips 500

# 맛 오름차순 and 버거가격 내림차순으로 정렬해서 출력하기
# fastfood=[
#     {'name':'mst','burger':3000,'chips':500,'tasty':'C'},
#     {'name':'mc','burger':5000,'chips':700,'tasty':'A'},
#     {'name':'bk','burger':7000,'chips':300,'tasty':'A'},
# ]
# print(sorted(fastfood, key=lambda x : (x['tasty'], -x['burger'])))
#

# 카운터 모듈 이용
# from collections import Counter
#
# a=[1,1,1,1,2,3,4]
# b=[1,1,2,3]
#
# print(Counter(a))
# print(Counter(b))
# print(Counter(a)-Counter(b))
# c=Counter(a)-Counter(b)
# print(list(c.items())[0])
# print(list(c.items())[0][1])

# hash 자료구조


# 폭탄 경로 문제
# arr = [
#     [0, 0, 0, 0, 0],
#     [0, 1, 3, 1, 0],
#     [0, 3, 0, 3, 0],
#     [0, 1, 3, 1, 0],
#     [0, 0, 0, 0, 0]
# ]
#
#
# # 새 배열에 벽:3 을 최신화
# new_arr = [[0]*5 for _ in range(5)]
# for i in range(5):
#     for j in range(5):
#         if arr[i][j] == 3:
#             new_arr[i][j] = 3
#
#
# directx = [1, -1, 0, 0]
# directy = [0, 0, 1, -1]
#
# def bfs(y1, x1):
#     queue = [(y1, x1, 0), (y1, x1, 1), (y1, x1, 2), (y1, x1, 3)]
#     new_arr[y1][x1] = 1
#     while queue:
#         y, x, dir = queue.pop(0)
#         dy = directy[dir] + y
#         dx = directx[dir] + x
#         if not(0 <= dx < 5 and 0<= dy < 5): continue
#         if arr[dy][dx] == 3: continue
#         new_arr[dy][dx] = 1
#         queue.append((dy,dx, dir))
#
# for i in range(5):
#     for j in range(5):
#         if arr[i][j] == 1:
#             bfs(i,j)
#
# cnt = 0
# for i in range(5):
#     for j in range(5):
#         if new_arr[i][j] == 0:
#             cnt += 1
# print(cnt)

arr = [1, 2, 3, 5, 4, 3]
part = []
for i in range(3):
    part.append(arr.pop())

part.sort()
print(part)
for i in range(len(part)):
    arr.append(part[i])
print(arr)