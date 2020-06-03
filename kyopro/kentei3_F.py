import itertools
from scipy.special import comb
n = int(input())
k =[]
kai =""
for x in range(n):
    k.append(list(map(str, input())))

k_l =list(itertools.chain.from_iterable(k))

for v in itertools.combinations(k_l n):
    if v == v[::-1]:
        for x in range(n):
            kai =''.join(v)
        print(kai)
        exit()

print("-1")