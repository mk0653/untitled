n = input()
kei = 0

for i in range(int(n)+1):
    if i%3 != 0 and i%5 != 0:
        kei += i

print(kei)