import copy

n = int(input())
list1 = list(map(int,input().split()))
list2 = copy.copy(list1)

for x in range(n):
    kei = 0
    list2 = copy.copy(list1)
    del list2[x]
    for m in range(n-1):
        l = list2.pop(0)
        if l in list2:
            kei += list2.count(l)

    print(kei,sep="\n")
