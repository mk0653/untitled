n = int(input())
m = list(map(int,input().split()))

a = 0
b = 0

m.sort(reverse=True)

while True:
    a += m.pop(0)
    if len(m) == 0:
        break
    b += m.pop(0)
    if len(m) == 0:
        break

print(a - b)
