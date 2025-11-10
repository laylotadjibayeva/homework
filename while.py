while True:
    rang = input("svetafor qaysi rangda?").lower()
    if rang in ["qizil", "sariq", "yashil"]:
        print("Rahmat, to‘g‘ri keladi!")
        break
    else:
        print("Bunday rang yo‘q, qayta urinib ko‘ring.")


# # Do‘stlar ro‘yxatini yaratish
# friends = []

# while True:
#     ism = input("Do‘stingiz ismini kiriting (to‘xtatish uchun 'stop' yozing): ")
#     if ism.lower() == "stop":
#         break
#     friends.append(ism)

# print("Sizning do‘stlaringiz ro‘yxati:")
# for friend in friends:
#     print(friend)


# # Valyuta ayirboshlash kalkulyatori
# kurs = 12600  # 1 USD = 12600 so‘m
#
# while True:
#     summa = input("So‘m miqdorini kiriting (yoki 'exit' yozing): ")
#
#     if summa.lower() == "exit":
#         print("Dastur tugadi.")
#         break
#     else:
#         som = int(summa)
#         dollar = som / kurs
#         print(f"{som} so‘m = {dollar:.2f} USD")