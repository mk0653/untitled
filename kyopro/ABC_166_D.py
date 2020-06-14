n = input()
n = int(n)

for x in range(10**5):
    for m in range(10):
        if x ** 5 + m ** 5 == n:
            print(x,-m)
            exit()
