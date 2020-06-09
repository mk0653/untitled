import collections

n = int(input())
k = list(map(int,input().split()))

c = collections.Counter(k)

for x in range(n):
    print(c[x+1])
