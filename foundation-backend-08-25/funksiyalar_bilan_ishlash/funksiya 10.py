# maxsulotlar=["Kartoshka","Piyoz", "Gosht","Pamidor", "Sabzi"]
# royxat=[]
# for maxsulot in maxsulotlar:
#     a=int(input("kerakli maxsuloylar indekisini kiriting: "))
#     x=maxsulotlar.pop(a)
#     royxat.append(x)
#     for maxsulot in maxsulotlar:
#         b=int(input("kerakli maxsuloylar indekisini kiriting: "))
#         y=maxsulotlar.pop(b)
#         royxat.append(y)
#         for maxsulot in maxsulotlar:
#             c=int(input("kerakli maxsuloylar indekisini kiriting: "))
#             z=maxsulotlar.pop(c)
#             royxat.append(z)
# print(royxat)

maxsulotlar=["Kartoshka","Piyoz","Rediska", "Gosht","Pamidor", "Sabzi","Karam","Baqlajon",]
royxat=[]
print(f"indeks boyicha tartiblanish '0'dan boshlanadi '7'da tugaydi", maxsulotlar)
for maxsulot in maxsulotlar:
    b=int(input("maxsulotlar indeksini kiriting: "))
    a=maxsulotlar.pop(b)
    royxat.append(a)
print(royxat)

