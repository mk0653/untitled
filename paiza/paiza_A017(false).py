h, w, n = map(int,input().split())
c= ""
m = []
q = []
for x in range(h):
    a = ""
    for l in range(w):
        a = a + "."
        c = c + "#"
    m.append(a)
for b in range(n):
    q.append(list(map(int, input().split())))

for p in range(n):
    for o in range(h):
        print(m[o][q[p][2] - 1: q[p][1] + q[p][2] - 1])
        if "#" in m[o][q[p][2]-1 : q[p][1]-1 + q[p][2] -1]:
            m[o -1] = m[o-1][0:q[p][2]] + c[0:q[p][2]] +m[o-1][q[p][2]+1:-1]
            break
        elif o == h-1:
            m[o] = m[o][0:q[p][2]] + c[0:q[p][1]-1] + m[o][q[p][1]:-1]
            print(m)

#for aa in range(h):
    #print(m[aa])
print(q)