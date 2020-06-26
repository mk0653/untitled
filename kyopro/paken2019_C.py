n,m = map(int,input().split())
k = []
kai = []
ans = 0
for x in range(n):
    k.append(list(map(int,input().split())))

for a in range(m):
    ans = 0
    seito = []
    for b in range(n):
        seito.append(k[b][a])
    kai.append(seito)

for c in range(m):
    for d in range(m):
        hikaku =0
        for e in range(n):
            hikaku += max(kai[c][e],kai[d][e])
            ans = max(ans, hikaku)

print(ans)