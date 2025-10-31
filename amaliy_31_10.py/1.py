class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other):
        if self.age < other.age:
            return f"{other.name} mendan katta."
        elif self.age > other.age:
            return f"{other.name} mendan kichik."
        else:
            return f"{other.name} men bilan teng yoshda."


p1 = Person("Sardor", 24)
p2 = Person("Jasur", 36)
p3 = Person("Laylo", 24)

print(p1.compare_age(p2))
print(p2.compare_age(p1))
print(p1.compare_age(p3))
