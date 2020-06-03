import re

n = input()
m = input()
k = re.match(n, m)

if k is  None:
    print("No")
    exit()

if len(n) != len(m) - 1  and k.group() != n:
    print("No")
else:
    print("Yes")
