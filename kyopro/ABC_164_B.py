n = list(map(int,input().split()))

tairyoku1 = n[0]
tairyoku2 = n[2]

while True:
    tairyoku2 = tairyoku2 - n[1]
    if tairyoku2 <= 0:
        print("Yes")
        exit()
    tairyoku1 = tairyoku1 - n[3]
    if tairyoku1 <= 0:
        print("No")
        exit()
