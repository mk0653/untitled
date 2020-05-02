import math

n = list(map(int,input().split()))
#hikaku = 0

#for x in range(1,n[2]+1):
#    m = math.floor(n[0] * x // n[1]) - n[0] * math.floor(x // n[1])
#    if hikaku < m:
#        hikaku = m

x = min(n[1]-1 , n[2])
if n[2] >= n[2]:
    print(math.floor(n[0] * x / n[1]))