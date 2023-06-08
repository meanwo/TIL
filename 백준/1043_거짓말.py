N, M = map(int, input().split())
tmp = list(map(int, input().split()))

# 처음부터 진실을 알고 있는 멤버
truth_member = set(tmp[1:])

party = []
for _ in range(M):
    members = list(map(int, input().split()))
    party.append(members[1:])




count = M
for _ in range(M):
    for i in range(len(party)):
        if set(party[i]) & truth_member:
            truth_member |= set(party[i])


for i in range(len(party)):
    if set(party[i]) & truth_member:
        count -= 1
print(count)

