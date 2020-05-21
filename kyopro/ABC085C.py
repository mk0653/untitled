n, y = list(map(int, input().split()))

kei = 0

for k in range(n+1):
    for l in range(n + 1 - k):
        kei = k * 10000 + l * 5000 + 1000 * (n-(k+l))
        if k + l + (n-(k+l)) == n and kei == y:
            print(k, l, n-(k+l))
            exit()

print("-1 -1 -1")
