n = list(map(int,input().split()))
kei = 0
l = []
for x in range(n[0]+1):
    l = list(str(x))
    l_si = [int(s) for s in l]
    if n[1] <= sum(l_si) <= n[2]:
        kei += x

print(kei)