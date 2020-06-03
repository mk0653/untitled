a, r, n = map(int, input().split())
kei = 0

if n > 10 and r > 10 and a >= 1:
    print("large")
    exit()
kei = a *r**(n-1)

if kei > 10**9:
    print("large")
else:
    print(kei)