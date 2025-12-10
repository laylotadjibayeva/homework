

#############2
import datetime as dt
# bugun = dt.date.today()
# ramazon = dt.date(2026, 3, 20)
# qurbon = dt.date(2026,5,27)
# farq_r = ramazon-bugun
# farq_q = qurbon-bugun
# print(f"Ramazon hayitiga {farq_r.days} kun qoldi")
# print(f"Qurbon hayitiga {farq_q.days} kun qoldi")



#############3
# tugilgan_kun = dt.date(2006,4,26)
# bugun = dt.date.today()
# yil = bugun.year - tugilgan_kun.year
# oy = bugun.month - tugilgan_kun.month
# kun = bugun.day - tugilgan_kun.day
# if kun < 0:
#     oy -= 1
#     kun += 30
#
# print(f"{yil} yil, {oy} oy, {kun} kun")



##############4
# import re
# phone = input("Telefon raqamingizni kiriting: ")
# andoza = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
# if re.match(andoza, phone):
#     print("Raqam to‘g‘ri!")
# else:
#     print("Raqam noto‘g‘ri")


################5
import re
matn = """An’anaviy pedagogika — bu https://www.google.com/ ta’limning qadimdan shakllangan
 klassik tizimi bo‘lib, unda asosiy e’tibor o‘quvchiga tayyor bilim, 
 ko‘nikma va malakalarni https://www.facebook.com/ berishga qaratiladi. Jarayonni o‘qituvchi boshqaradi
  va nazorat qiladi. O‘quvchi esa asosan bilimni qabul qiluvchi 
va qayta ishlab beruvchi sifatida qatnashadi.
."""

andoza = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()!@:%_+.~#?&/=]*)'

url = re.findall(andoza, matn)
print(url)


