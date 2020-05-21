n = list(map(int,input().split()))
ki = []
gu = []
count = 0

for x in range(3):
    if n[x] %2 == 0:
        ki.append(x)
    else:
        gu.append(x)

if len(gu) < len(ki) != 3:
    n[ki[0]] += 1
    n[ki[1]] += 1
    count +=1
elif len(ki) < len(gu) != 3:
    n[gu[0]] += 1
    n[gu[1]] += 1
    count +=1


n.sort(reverse=True)
count += (n[0] -n[1]) / 2
count += (n[0] -n[2]) / 2

print(int(count))