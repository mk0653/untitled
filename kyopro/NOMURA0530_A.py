n = list(map(int,input().split()))

start = n[0]*60 + n[1]
end = n[2]*60 + n[3]

zikan = (end - start) - n[4]
print(zikan)


