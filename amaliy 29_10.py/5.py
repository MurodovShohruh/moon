class Ayiq:
    def __init__(self, nomi, vazni, turi):
        self.nomi = nomi
        self.vazni = vazni
        self.turi = turi

    def ovqatlanish(self):
        print(f" {self.nomi} ({self.turi} qor odam) asal, baliq va mevalar yeyapti!")

    def uxlash(self):
        print(f" {self.nomi} hozir dam ovlayapti, panada kutayapti.")


ayiq1 = Ayiq("Bobur", 100, "qora")


print(f"Ayiq nomi: {ayiq1.nomi}")
print(f"Vazni: {ayiq1.vazni} kg")
print(f"Turi: {ayiq1.turi}")


ayiq1.ovqatlanish()
ayiq1.uxlash()
