n = list(map(int,input().split()))
m = list(map(int,input().split()))

m.sort(reverse=True)
kyori = []
for x in range(n[1]-1):
    kyori.append(m[x]-m[x+1])

kyori.append((m[len(m)-1]+n[0])-m[0])
print(sum(kyori)-max(kyori))