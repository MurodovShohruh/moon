
class Mashina:
    def __init__(self, marka, model, tezlik):
        self.marka = marka
        self.model = model
        self.tezlik = max(0, tezlik)  

    def tezlash(self):
    
        self.tezlik += 10
        print(f"{self.marka} {self.model} hozirgi tezligi: {self.tezlik} km/soat")

    def info(self):
        print(f"Nomi: {self.marka}, modeli: {self.model}, tezligi: {self.tezlik} km/soat")

mashina1 = Mashina("FORD", 2025, 0)

mashina1.info()

for i in range(36):  
    mashina1.tezlash()
