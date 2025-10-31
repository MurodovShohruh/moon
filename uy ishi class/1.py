royxat=[]

class Student_info:
    def __init__(self,kursi, ism=None, yosh=None, qarori=None, ball=None ,jami = None):
        self.ism = ism
        self.yosh = yosh
        self.kursi = kursi
        self.ball_value = ball
        self.qaror_value = qarori
        self.jami_ballar = jami


    def ism_kiritish(self):
        self.ism = input("Ismini kiriting: ")

    def yosh_kiritish(self):
        self.yosh = input("Yoshini kiriting: ")

    def ball_kiritish(self):
        self.ball_value = input(f"{self.ism} qancha ball olganini kiriting: ")
        print(f"{self.ism} natijasi: '{self.ball_value}!'")

    def n_olish(self):
        print(f"{self.ism}, natijasiga rozimi?")

    def qaror(self):
        self.qaror_value = input(f"{self.ism}, 'Ha' yoki 'Yo'q' deb yozing: ")
        print(f"{self.ism}, tanloving qabul qilindi!")
    
    def jami_ball(self):
        self.jami_ballar=input("Olgan ballarini kiriting: ").split()
        for n in self.jami_ballar:
            royxat.append(float(n))

Student = Student_info( "Backend")

Student.ism_kiritish()
Student.yosh_kiritish()

print(f"Kursi: {Student.kursi}")

Student.jami_ball()

print(f"O'rtacha ball: {sum(royxat)/len(royxat):.3f}")

Student.ball_kiritish()
Student.n_olish()
Student.qaror()

