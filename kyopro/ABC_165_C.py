from itertools import *

n = list(map(int,input().split()))
mm =[]
list1 = []
kei  = []

for x in range(n[2]):
    m = list(map(int,input().split()))
    mm.append(m)

for x in range(n[1]):
    list1.append(x+1)

a = list(combinations_with_replacement(list1,n[0]))

for x in range(len(a)):
    count = 0
    for l in range(n[2]):
        if a[x][int(mm[l][1]-1)] - a[x][int(mm[l][0]-1)] == int(mm[l][2]):
            count += int(mm[l][3])
    kei.append(count)

print(max(kei))