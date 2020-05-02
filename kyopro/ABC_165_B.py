n = int(input())

ginko = 100
count = 0

while True:
    ginko += ginko // 100
    count += 1
    if ginko >= n:
        print(count)
        break