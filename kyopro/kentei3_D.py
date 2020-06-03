n = int(input())
k =[]
for x in range(5):
    k.append(list(map(str, input())))
aa = n*4
zen =[] * ((4 * n+1) - (n+1))
kai =[""] * aa
for l in range(5):
    hantei = []
    iti = 0
    for m in range(4*n + 1):
        if m >= 1 and m%4 != 0:
            if k[l][m] == "#":
                hantei.append("1")
            else:
                hantei.append("0")
        if len(hantei) == 3:
            kai[iti] += hantei

    #zen.append(hantei)

print(kai)

#0:111 101 101 101 111
#1:010 110 010 010 111
#2:111 001 111 100 111
#3:111 001 111 001 111
#4:101 101 111 001 001
#5:111 100 111 001 111
#6:
#　省かれる数N+1個