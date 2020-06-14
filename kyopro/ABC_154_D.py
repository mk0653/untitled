n, k = input().split()
m = list(map(int, input().split()))

kazu =[]
kai = []
kazu = [(a+1) /2 for a in m]
kitai = sum(kazu[0:int(k)])
ans = kitai


for x in range(int(n) - int(k)):
    kitai -= kazu[x]
    kitai += kazu[x + int(k)]
    if ans < kitai:
        ans = kitai

print(ans)