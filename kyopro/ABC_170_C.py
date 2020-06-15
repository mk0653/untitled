x, n = input().split()
x = int(x)
n = int(n)
m = list(map(int,input().split()))
sa = 999
ans = 0

if m.count(x) == 0 :
    print(x)
    exit()
elif len(m) == 0:
    print(x)
    exit()

for k in range(1,200):
    if m.count((x - k)) == 0 and x - (x - k) < sa:
        sa =  x - (x - k)
        ans = x - k

for l in range(1,200):
    if m.count((x + l)) == 0 and (x+l) - x < sa:
        sa = (x+l) - x
        ans = x + l

print(ans)