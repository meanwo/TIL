# N은 열
# M은 행
N, M = map(int, input().split())
num = int(input())
spot = []
for i in range(num):
    a, b = map(int, input().split())
    spot.append((a, b))
loc = list(map(int, input().split()))

print(spot)
print(loc)
distance = 0
for i in range(num):
    if spot[i][0] == loc[0]:
        distance += abs(loc[1]-spot[i][1])
    elif (loc[0], spot[i][0]) == (3, 4) or (loc[0], spot[i][0]) == (4, 3):
        if loc[1]+spot[i][1] < M:
            distance += N+loc[1]+spot[i][1]
        else:
            distance += N + 2*M - (loc[1]+spot[i][1])
    elif (loc[0], spot[i][0]) == (1, 2) or (loc[0], spot[i][0]) == (2, 1):
        if loc[1]+spot[i][1] < N:
            distance += M+loc[1]+spot[i][1]
        else:
            distance += M + 2*N - (loc[1]+spot[i][1])
    elif (loc[0], spot[i][0]) in ((1, 3), (3, 1)):
        distance += spot[i][1]+loc[1]
    elif (loc[0], spot[i][0]) in ((2, 4), (4, 2)):
        distance += M+N-spot[i][1]-loc[1]
    elif (loc[0], spot[i][0]) == (4, 1):
        distance += N-spot[i][1]+loc[1]
    elif (loc[0], spot[i][0]) == (1, 4):
        distance += N+spot[i][1]-loc[1]
    elif (loc[0], spot[i][0]) == (2, 3):
        distance += M+loc[1]-spot[i][1]
    elif (loc[0], spot[i][0]) == (3, 2):
        distance += M-loc[1]+spot[i][1]



print(distance)