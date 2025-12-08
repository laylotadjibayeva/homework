tugilgan_kun = "26042006"
with open('pi_million_digits.txt',"r") as fayl:
    pi = fayl.read()

if tugilgan_kun in pi:
    print("Tug'ilgan kun faylda bor")
else:
    print("Tug'ilgan kun faylda yo'q")
