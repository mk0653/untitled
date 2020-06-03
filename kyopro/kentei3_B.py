n,m,q = map(int,input().split())
toi = [n]*m
ten = [[0]*m for i in range(n)]
k =[]
for x in range(q):
    k .append(list(map(int, input().split())))

for x in range(q):
     if k[x][0] == 2:
        if toi[k[x][2]-1] != 0:
            toi[k[x][2]-1] = toi[k[x][2]-1] - 1
        ten[k[x][1] - 1][k[x][2] - 1] = 1
     else:
         kei = 0
         for l in range(m):
             if ten[k[x][1] - 1][l] >= 1:
                kei += toi[l]
         print(kei)
