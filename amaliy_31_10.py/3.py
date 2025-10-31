class Player:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return f"{self.name} {self.age} yoshda"

    def get_height(self):
        return f"{self.name} bo‘yi {self.height} sm"

    def get_weight(self):
        return f"{self.name} vazni {self.weight} kg"


p1 = Player("David Jones", 25, 175, 75)
print(p1.get_age())
print(p1.get_height())
print(p1.get_weight())
