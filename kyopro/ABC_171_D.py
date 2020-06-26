import collections

n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = []
for x in range(q):
    b.append(list(map(int, input().split())))

hikaku = 0
a_wa = sum(a)
cou = collections.Counter(a)
for i in range(q):
    a_wa += cou[b[i][0]] * b[i][1] - cou[b[i][0]] * b[i][0]
    cou[b[i][1]] += cou[b[i][0]]
    cou[b[i][0]] = 0

    print(a_wa)
