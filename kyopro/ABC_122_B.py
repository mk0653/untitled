import copy

n = input()
m = copy.copy(n)
ans = 0

for x in range(len(n)):
    for l in range(len(n)):
            mm = m[x:len(n)-l]
            if mm.count("A") + mm.count("C") + mm.count("G")+ mm.count("T") == len(mm):
                ans = max(ans, len(mm))

print(ans)