# ######1
# def foydalanuvchi_malumotlari(telefon=None, email=None):
#     """Foydalanuvchi ma'lumotlarini olib, yoshni tug'ilgan yil orqali hisoblaydi"""

#     hozirgi_yil = 2025
#     ism = input("Ismingizni kiriting: ")
#     familiya = input("Familiyangizni kiriting: ")
#     tugilgan_yil = int(input("Tug'ilgan yilingiz: "))
#     tugilgan_joy = input("Tug'ilgan joyingiz: ")

#     yosh = hozirgi_yil - tugilgan_yil

#     if telefon is None:
#         telefon = input("Telefon raqamingiz (ixtiyoriy): ")

#     if email is None:
#         email = input("Email manzilingiz (ixtiyoriy): ")

#     foydalanuvchi = {
#         "ism": ism,
#         "familiya": familiya,
#         "tugilgan_yil": tugilgan_yil,
#         "tugilgan_joy": tugilgan_joy,
#         "yosh": yosh,
#         "telefon": telefon,
#         "email": email
#     }

#     return foydalanuvchi

# # a = foydalanuvchi_malumotlari()
# # print(a)

# ######2
# mijozlar = []

# while True:
#     print("\n Yangi mijoz ma'lumotlari ")
#     mijozlar.append(foydalanuvchi_malumotlari())

#     davom = input("Yana mijoz kiritilsinmi? (ha/yo'q): ")
#     if davom.lower() == "yo'q":
#         break

# print("\nKiritilgan mijozlar:")
# for m in mijozlar:
#     print(m)


# ######3
# def eng_katta(a, b, c):
#     return max(a, b, c)

# a = float(input("1-sonni kiriting: "))
# b = float(input("2-sonni kiriting: "))
# c = float(input("3-sonni kiriting: "))

# print("Eng katta son:", eng_katta(a, b, c))


# ######4
# import math

# def aylana_info(r):
#     diameter = 2 * r
#     perimetr = 2 * math.pi * r
#     yuza = math.pi * (r ** 2)

#     return {
#         "radius": r,
#         "diametr": diameter,
#         "perimetr": perimetr,
#         "yuza": yuza
#     }

# print(aylana_info(5))


# #######5
# def tub_sonlar(bosh, oxir):
#     tublar = []

#     for son in range(bosh, oxir + 1):
#         if son > 1:
#             tub = True
#             for i in range(2, son):
#                 if son % i == 0:
#                     tub = False
#                     break
#             if tub:
#                 tublar.append(son)

#     return tublar

# print(tub_sonlar(1, 50))


# #######6

# def fibonacci(n):
#     fib = [1, 1]

#     for i in range(2, n):
#         yangi_son = fib[i-1] + fib[i-2]
#         fib.append(yangi_son)

#     return fib[:n]


# print(fibonacci(10))