m=int(input())
n=[int(input()) for i in range(int(m))]

n.sort(reverse=True)
yaki1 = 0
yaki2 = 0

for l in range(m):
    if(yaki1 <= yaki2) :
        yaki1 += int(n[l])
    else:
        yaki2 += int(n[l])

if yaki1 >= yaki2:
    print(yaki1)
else:
    print(yaki2)