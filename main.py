# 4-m
class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif

    def info(self):
        print("kitob nomi chiqaradi")

class Darslik(Kitob):
    def info(self):
        super().info()
        print("Bu darslik")

d1 = Darslik("O'tkan kunlar", "aggdafg")
d1.info()


# 7-m
class Ota:
    def __init__(self, ism):
        self.ism = ism

    def gapir(self):
        print("Gapirdi")

class Ogil(Ota):
    def gapir(self):
        super().gapir()
        print("Ogil gapirdi")

o1 = Ogil("Sobirjon")
o1.gapir()

