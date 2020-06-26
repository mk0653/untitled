n = int(input())
m = list(map(int, input().split()))

hantei = 10 ** 18
kekka = 1
m.sort()
for x in range(n):
    kekka = kekka * m[x]
    if kekka > hantei:
        print("-1")
        exit()

print(kekka)