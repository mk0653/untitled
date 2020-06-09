n, m = input().split()
k = list(map(int,input().split()))

if sum(k) > int(n):
    print("-1")
    exit()

kekka = int(n) - sum(k)

print(kekka)