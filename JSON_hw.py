import json

##################1,2,3
# data = {"Model" : "Malibu", "Rang": "Qora", "Yil":2020, "Narh":40000}
# with open("data.json", "w") as file:
#     json.dump(data, file)



# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# talaba = json.loads(talaba_json)
# print(talaba['ism'])
# print(talaba['familiya'])
# with open("talaba.json", "w") as file:
#     json.dump(talaba, file)


##############4
with open("students.json", "r", encoding="utf-8") as file:
    student = json.load(file)

    student1 = student[0]
    student2 = student[1]
    student3 = student[2]

print(f"{student1['name']} {student1['lastname']}, {student1['year']}-kurs, {student1['faculty']} talabasi")
print(f"{student2['name']} {student2['lastname']}, {student2['year']}-kurs, {student2['faculty']} talabasi")
print(f"{student3['name']} {student3['lastname']}, {student3['year']}-kurs, {student3['faculty']} talabasi")


