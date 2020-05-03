m = int(input())
n = [input() for i in range(m)]

nn = list(set(n))

print(len(nn))