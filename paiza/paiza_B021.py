n = int(input())
m = []
kai = None

for x in range(n):
    m.append(input())

for x in range(n):
    if m[x].endswith(('s','sh','ch',"o","x")) :
        kai = m[x] + "es"
    elif m[x].endswith("f"):
        kai = m[x][0:len(m[x])-1] + "ves"
    elif m[x].endswith("fe"):
        kai = m[x][0:len(m[x]) -2] + "ves"
    elif m[x].endswith(("ay","iy","uy","ey","oy")) == False and m[x].endswith("y") == True:
        kai = m[x].rstrip("y") + "ies"
    else:
        kai = m[x] + "s"

    print(kai)