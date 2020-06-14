import copy
n,m = input().split()
moti = [[] for j in range(int(m))]
for x in range(int(n)):
    moti[x] = [int(m) for m in input().split()]

hantei2 = 0
ans = 0

for a in range(2 ** (int(n))):
    omoti = []
    for b in range(int(n)):
        if ((a >> b) & 1):
            omoti.append([1 - moti[b][k] for k in range(int(m))])
        else:
            omoti.append([moti[b][k] for k in range(int(m))])

    motikazu = 0
    for o in range(int(m)):
        motikazu += max(sum([omoti[p][o] for p in range(int(n))]), int(n) - sum([omoti[p][o] for p in range(int(n))]))
    ans = max(motikazu,ans)

print(ans)
