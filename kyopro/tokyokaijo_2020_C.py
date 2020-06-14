import math,copy
n, k = input().split()
n =int(n)
k =int(k)
m = list(map(int, input().split()))
mm = copy.deepcopy(m)

for x in range(k):

    for q in range(len(m)):
        ato = math.ceil(m[q] + 0.5)
        for z in range(ato):
            if min(q+(z+1),len(m)-1) != q:
                mm[min(q+(z+1),len(m)-1)] += 1
            if max(q-(z+1),0) != q:
                mm[max(q-(z+1),0)] += 1
    m = copy.deepcopy(mm)

print(m)



