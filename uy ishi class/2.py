class Car_info:
    def __init__(self,yil,rusum=None,narx=None):
        self.rusumi=rusum
        self.yili=yil
        self.narxi=narx
    
    def rusumi_1(self):
        self.rusumi=input(f"Tanlangan mashina rusumini kiriting: ")

    def narxi_1(self):
        self.narxi=input("Mashinaning narxi: $ ")

cars = Car_info ("2024")

cars.rusumi_1()

print(f"Mashina yili: {cars.yili}")

cars.narxi_1()

print(f"Mashina rusumi: {cars.rusumi}, yili: {cars.yili}, narxi: ${cars.narxi}")

class Mijoz:
    def __init__(self,ismi=None,id=None):
        self.isim=ismi
        self.id1=id

    def mijoz_1(self):
        self.isim=input("Mijozning ismi: ")
    
    def id_1(self):
        self.id1=input(f"{self.isim} id raqamini kirgizing:  ")

mijoz1=Mijoz()

mijoz1.mijoz_1()
mijoz1.id_1()

print(f"Mijoz {mijoz1.isim} id raqami {mijoz1.id1}")

class ijara:
    def __init__(self):
        pass