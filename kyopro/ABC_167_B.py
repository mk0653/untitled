n = list(map(int,input().split()))

if n[0] >= n[3]:
    print(n[3])
elif n[0]+n[1] >= n[3]:
    print(n[0])
else:
    print(n[0] - (n[3]-(n[0]+n[1])))
