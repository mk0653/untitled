import sys

n = int(input())

buf = 0            #嬉しさポイント
m = 0               #残金

if n == 0:
    print("0")
    sys.exit()

def check(x,buf):
    if x >= 500:
        m = x%500
        buf += (x//500)*1000
        buf = check(m,buf)
        return buf
    elif 0 < x >= 5:
        buf += (x//5)*5
        return buf
    else:
        return buf

kei = check(n,buf)
print(kei)