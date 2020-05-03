n = list(map(int,input().split()))
m = list(map(int,input().split()))

a = []
kaku = []
for x in range(n[1]) :
    a.append(list(map(int, input().split())))

kaku = [0]* len(m)
cou = 0

for x in range(n[1]):
    if m[a[x][0] -1 ] > m[a[x][1] -1 ]:
        kaku[a[x][0] -1 ] += 1
    else:
        kaku[a[x][0] - 1] -= 100000

    if m[a[x][1] -1 ] > m[a[x][0] -1 ]:
        kaku[a[x][1] -1 ] += 1
    else:
        kaku[a[x][1] - 1] -= 100000

for x in range(len(m)):
    if kaku[x] >= 0 :
        cou += 1

print(cou)
