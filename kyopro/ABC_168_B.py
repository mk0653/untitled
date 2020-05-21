n = int(input())
m = input()

if len(m) <= n :
    print(m)
else:
    print(m[:n]+"...")