n, a, b = map(int,input().split())
k=0
l=0

k = a * (n // (a+b))
l = min(n % (a + b),a)

print(k + l)