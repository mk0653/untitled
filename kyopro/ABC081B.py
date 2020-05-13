n = int(input())
m = list(map(int,input().split()))

flag = 0
count = 0
while True:
    for x in range(n):
        if m[x] % 2 == 0:
            m[x] = m[x] / 2
        else:
            flag += 1
    if flag > 0:
        break
    else:
        count += 1

print(count)