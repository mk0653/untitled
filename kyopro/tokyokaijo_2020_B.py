n = list(map(int,input().split()))
m = list(map(int,input().split()))
k = int(input())

if n[0] < m[0]:
    if n[0] + n[1] * k >= m[0] + m[1] * k:
        print("YES")
        exit()
elif n[0] > m[0]:
    if n[0] - n[1] * k <= m[0] - m[1] * k:
        print("YES")
        exit()

print("NO")