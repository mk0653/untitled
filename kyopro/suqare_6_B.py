from statistics import median
import math
n = int(input())
k = []
iri = []
de = []
zikan = 0
for x in range(n):
    k.append(list(map(int,input().split())))
    iri.append(k[x][0])
    de.append(k[x][1])

iriguti = math.ceil(median(iri))
deguti = math.ceil(median(de))

for a in range(n):
    zikan += abs(iriguti -k[a][0]) + abs(k[a][0] - k[a][1]) + abs(k[a][1] - deguti)

print(zikan)
