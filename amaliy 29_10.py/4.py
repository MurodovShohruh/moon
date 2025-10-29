class Odam:
    def __init__(self, ism, yosh, kasb):
        self.ism = ism
        self.yosh = yosh
        self.kasb = kasb

    def salom_ber(self):
        print(f"Salom! Mening ismim {self.ism}, yoshim {self.yosh} da.")

    def mehnat_qil(self):
        print(f"{self.ism} hozir {self.kasb} blan shug'ulanadi ")


odam1 = Odam("Bobur", 17, "Hakker")


print(f"Odamning ismi: {odam1.ism}")
print(f"Yoshi: {odam1.yosh}")
print(f"Kasbi: {odam1.kasb}")


odam1.salom_ber()
odam1.mehnat_qil()
