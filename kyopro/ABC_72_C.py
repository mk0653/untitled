import collections

n = int(input())
m = list(map(int,input().split()))

zen = m
cou = 0

for x in range(n):
    zen.append(m[x]-1)

for x in range(n):
    zen.append(m[x]+1)

a = collections.Counter(zen)

#for k in range(n):
#    if a.most_common()[0][0] == m[k] or a.most_common()[0][0] == m[k] -1 or a.most_common()[0][0] == m[k] +1:
#        cou += 1

print(a.most_common()[0][1])