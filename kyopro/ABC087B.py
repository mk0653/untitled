n = []
count = 0
for x in range(4):
    n.append(int(input()))

for a in range(n[0]+1):
    for b in range(n[1]+1):
        for c in range(n[2]+1):
            if a * 500 + b * 100 + c * 50 == n[3]:
                count += 1
print(count)