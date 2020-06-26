n, k = map(int, input().split())
m = list(map(int, input().split()))
kei = 0
m.sort()

for x in range(k):
    kei += m[x]

print(kei)
