import math

n = list(map(int,input().split()))

kaku = n[2] * 30 + n[3] * 0.5 - 6 *n[3]

if kaku >= 180:
    kaku = 360 - kaku

x = n[0]**2 + n[1]**2 - 2*n[0]*n[1] * math.cos(math.radians(kaku))
hen = math.sqrt(x)
#print(kaku)
print(hen)
