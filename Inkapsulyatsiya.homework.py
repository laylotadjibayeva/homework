class Shaxs:
    odamlar_soni = 0

    def init(self, ism, yosh):
        self.ism = ism
        self.__yosh = yosh
        Shaxs.odamlar_soni += 1

    def get_yosh(self):
        return self.__yosh

    def set_ism(self, ism):
        self.__ism = ism

    def get_odamlar_soni(self):
        return Shaxs.odamlar_soni


class Talaba(Shaxs):
    talabalar_soni = 0

    def __init(self, ism, yosh, id_raqam):
        super().init(ism, yosh)
        self.__id = id_raqam
        Talaba.talabalar_soni += 1

    def set_id(self, id_raqam):
        self.__id = id_raqam

    def get_talabalar_soni(self):
        return Talaba.talabalar_soni


s1 = Shaxs("Ali", 25)
s2 = Shaxs("Vali", 21)
t1 = Talaba("Laylo", 20, "L123")
t2 = Talaba("Shukurjon", 22, "Sh123")

print("Shaxslar soni:", t1.get_odamlar_soni())
print("Talabalar soni:", t2.get_talabalar_soni())