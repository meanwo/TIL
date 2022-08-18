A = [3, 1, 2, 1, 3, 2, 1, 2, 1]

n = int(input())

def jump(level):
    if level > 8:
        return
# arr = [2, 0, 1, 1, 3, 5, 1]
    jump(level+A[level])
    print(jump[level])

result = jump(n)