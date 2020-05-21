n = input()

m = list(n)
mm = list(reversed(m))

if mm[0] == "2" or mm[0] == "4" or mm[0] == "5" or mm[0] == "7" or mm[0] == "9" :
    print("hon")
elif mm[0] == "0" or mm[0] == "1" or mm[0] == "6" or mm[0] == "8":
    print("pon")
else:
    print("bon")
