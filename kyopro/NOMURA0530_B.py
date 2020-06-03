import  copy
n = list(input())
hantei = ["P", "D"]
taihi = copy.copy(n)
hakase = 0
ke = 0
aa = 0


def my_index(l, a, default=False):
    if a in l:
        return l.index(a)
    else:
        return default


def dp(x, kekka):
    iti = 0
    count1 = 0
    count2 = 0
    for m in range(2):
        n = taihi
        if n.count("?") != 0:
            iti = my_index(n, "?")
            n[iti] = hantei[m]

        if n.count("?") == 0:
            for l in range(len(n) - 1):
                ll = 0
                lk = 0
                while "D" == n[l + ll + 1]:
                    count1 += 1
                    if ll + l < len(n) - 1:
                        ll += 1
                    else:
                        break
                while "DP" == n[l + lk:l + lk + 1]:
                    count2 += 1
                    if lk + l < len(n) - 1:
                        lk += 1
                    else:
                        break
            if kekka < count1 + count2:
                kekka = count1 + count2
        else:
            dp(n,kekka)
    return (kekka)


aa = dp(n, ke)
print(aa)
