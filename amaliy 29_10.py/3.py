class Kema:
    def __init__(self, nomi, turi, yonalish):
        self.nomi = nomi
        self.turi = turi
        self.yonalish = yonalish

    def suzishni_boshlash(self):
        print(f" {self.nomi} ({self.turi}) kemasi {self.yonalish} yo'nalishi bo'yicha suzishni boshladi!")

    def toxtash(self):
        print(f" {self.nomi} kemasi manzilga yetib keldi va to'xtadi.")

kema1 = Kema("Qiruvchi", "Hodimlari", "Atlantika okeani")

print(f"Kema nomi: {kema1.nomi}")
print(f"Kema turi: {kema1.turi}")
print(f"Kema yo'nalishi: {kema1.yonalish}")

kema1.suzishni_boshlash()
kema1.toxtash()
