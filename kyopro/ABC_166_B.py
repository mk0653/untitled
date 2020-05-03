n = list(map(int,input().split()))
m= []
mm= []
nuke = []
for x in range(n[1]):
    m.append(int(input()))
    mm.extend(list(map(int,input().split())))

for i in range(n[0]):
    nuke.append(i+1)

mn = list(set(mm))

for l in range(len(mn)):
    if mn[l] in nuke:
        nuke.remove(mn[l])

print(len(nuke))