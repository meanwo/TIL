# tree
#
# 트리의 순회 (탐색하면서 출력순서)
# preorder  전위순회
# postorder 후위순회
# inorder   중위순회

arr=" ABCDEFG"

def preorder(now):

    if now>len(arr)-1: return
    print(arr[now],end=' ')
    preorder(now*2)
    preorder(now*2+1)

def postorder(now):

    if now>len(arr)-1: return

    postorder(now*2)
    postorder(now*2+1)
    print(arr[now], end=' ')

def inorder(now):

    if now>len(arr)-1: return

    inorder(now*2)
    print(arr[now], end=' ')
    inorder(now*2+1)


preorder(1) # 전위순회
print()
postorder(1) # 후위순회
print()
inorder(1) # 중위순회

# heap sort 구현
# maxheap
# arr=[4,7,9,1,3,8,44,13]
# heap=[0]*20     # MAX HEAP    1차원 리스트
# hindex=1
#
# def insert(value):
#     global heap,hindex
#     heap[hindex]=value
#     now=hindex
#     hindex+=1
#
#     while 1:
#         parents=now//2
#         if parents==0: break
#         if heap[parents]>=heap[now]: break      # 수정
#         heap[parents],heap[now]=heap[now],heap[parents]
#         now=parents
#
#
#
# def top():
#     global heap
#     return heap[1]
#
# def pop():
#     global heap,hindex
#     heap[1]=heap[hindex-1]
#     heap[hindex]=0          # 수정
#     hindex-=1
#
#     now=1
#     while 1:
#         son=now*2
#         rson=son+1
#
#         if rson<=hindex and heap[son]<heap[rson]: son=rson  # 수정
#         if son>hindex or heap[now]>heap[son]: break         # 수정
#         heap[now],heap[son]=heap[son],heap[now]
#         now=son
#
# for i in range(len(arr)):
#     insert(arr[i])          # 이진트리의 형태로 저장을 하는
#
# for i in range(len(arr)):
#     print(top(),end=' ')    # 1번인덱스 출력
#     pop()                   # 트리에서 값 제거 후 자식들과 비교
