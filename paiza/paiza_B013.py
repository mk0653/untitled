a, b, c = map(int,input().split())
n = int(input())
m = []
ti = 60 * 8 +59
kai = 0
zikoku =[]
for x in range(n):
    m.append(list(map(int,input().split())))

for l in range(n):
    sou = 0
    sou += m[l][0] * 60 + m[l][1] + b + c
    if ti > sou > kai:
        kai = sou
        zikoku = m[l]

kai = zikoku[0] *60 + zikoku[1] -a
if kai%60 >= 10:
    print("0"+str(kai//60)+":"+str(kai%60))
else:
    print("0" + str(kai // 60) + ":0" + str(kai % 60))