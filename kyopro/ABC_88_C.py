n = []
m = [[0 for i in range(3)] for j in range(2)]
for x in range(3):
    n.append(list(map(int, input().split())))

k =max(n)
kaisuu = max(k) + 1

def tansa(m):
    iti = 2
    for j in range(kaisuu):
        for k in range(kaisuu):
            if j + k == n[iti][iti]:
                m[0][iti] = j
                m[1][iti] = k
                for a in range(kaisuu):
                    for b in range(kaisuu):
                        if a + b == n[iti - 1][iti - 1] and a + m[1][iti] == n[iti - 1][iti]:
                            m[0][iti - 1] = a
                            m[1][iti - 1] = b
                            for c in range(kaisuu):
                                for d in range(kaisuu):
                                    if c + d == n[iti - 2][iti - 2] and c + m[1][iti - 1] == n[iti - 2][iti - 1] and c + m[1][iti] == n[iti - 2][iti]:
                                        m[0][iti-2] = c
                                        m[1][iti-2] = d
                                        if m[0][1] + m[1][0] == n[1][0] and m[0][2] + m[1][0] == n[2][0] and m[0][2] + \
                                                m[1][1] == n[2][1]:
                                            print("Yes")
                                            exit()

tansa(m)
print("No")
