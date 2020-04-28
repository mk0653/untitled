n = input()

list1 = [str(x) for x in n]
list2 = []
list3 = []
matu = 0

for x in range(int((len(n)-1)//2)):
    list2.append(n[x])

for x in range(int(len(n)-(len(n)+3)//2 + 1)):
    matu = len(n) - x -1
    list3.append(n[matu])

list2_ke = ''.join(list2)
list3_ke = ''.join(list3)

if list1 == list(reversed(n)) and list2 == list(reversed(list2_ke)) and list3 == list(reversed(list3_ke)) :
    print("Yes")

else :
    print("No")