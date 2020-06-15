x, y = input().split()
x = int(x)
y = int(y)

for m in range(x+1):
    if y == (x - m) * 4 + m * 2:
        print("Yes")
        exit()

print("No")
