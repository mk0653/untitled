import math
a, b = map(int,input().split())
ans = []

for x in range(1,1009):
    if math.floor(x * 0.08 )== a and math.floor(x * 0.1) == b:
        ans.append(x)

if len(ans) == 0:
    print("-1")
else:
    print(min(ans))