###1
class User:
    def init(self, ism, username, email):
        self.ism = ism
        self.username = username
        self.email = email

    def get_info(self):
        print( f"Foydalanuvchi: Ismi {self.ism}, : Username {self.username}, Email {self.email}.")

Foydalanuvchi1 = User("alijon", "alijon1994", "alijon1994@gmail.com")
Foydalanuvchi2 = User("laylo", "laylo2000", "laylo2000@mail.ru")

Foydalanuvchi1.get_info()
Foydalanuvchi2.get_info()


###2