import collections

n = int(input())
list1 = list(map(int,input().split()))
list2 = collections.Counter(list1)

kei1=0

for j in list2.values():
    kei1 += j * (j-1) // 2

for x in list1:
    print(kei1 - (list2[x] -1))