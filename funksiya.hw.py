# 1
def tugilgan_yil():
    ism = input("Ismingizni kiriting: ")
    yosh = int(input("Yoshingizni kiriting: "))
    yil = 2025 - yosh
    print(f"{ism}, siz {yil}-yilda tug‘ilgansiz./")

tugilgan_yil()


# 2
def kvadrat_kub():
    son = float(input("Biror son kiriting: "))
    print(f"{son} ning kvadrati = {son**2}")
    print(f"{son} ning kubi = {son**3}")

kvadrat_kub()


# 3
def juft_yoq_toq():
    son = int(input("Son kiriting: "))
    if son % 2 == 0:
        print(f"{son} juft son.")
    else:
        print(f"{son} toq son.")

juft_yoq_toq()


# 4
def katta_sonni_top():
    a = float(input("1-sonni kiriting: "))
    b = float(input("2-sonni kiriting: "))
    if a > b:
        print(f"{a} katta {b} dan.")
    elif a < b:
        print(f"{b} katta {a} dan.")
    else:
        print("Sonlar teng.")

katta_sonni_top()


# 5
def daraja(x, y):
    print(f"{x}^{y} = {x  y}")

daraja(3, 4)


# 6
def daraja_standart(x, y=2):
    print(f"{x}^{y} = {x  y}")

daraja_standart(5)
daraja_standart(3, 3)


# 7
def bolinish_alomatlari(son):
    for n in range(2, 11):   # 2 dan 10 gacha
        if son % n == 0:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(70)