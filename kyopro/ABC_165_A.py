n = int(input())
m = list(map(int,input().split()))

sa = m[1] - m[0]
flag = 0
hantei = m[0]

if sa == 0:
    if m[0] % n == 0:
        print("OK")
        exit()
    else:
        print("NG")
        exit()

if hantei % n == 0:
    flag += 1

for x in range(sa):
    hantei = (x + 1) + m[0]
    if hantei % n == 0:
        flag += 1

if flag >= 1:
    print("OK")
else:
    print("NG")