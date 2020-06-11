n = int(input())
ans = 0


for x in range(1,n+1,2):
    cou = 0
    for j in range(1,x+1):
        if x % j == 0:
            cou += 1
    if cou == 8:
        ans += 1

print(ans)