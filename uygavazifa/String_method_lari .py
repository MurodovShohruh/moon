#  relation_to_luke.py

# def eslatma():
#     isim=input("Isimni kiriting = ")
#     if isim == "Darth Vader":
#         return f"{isim} men sening otangman !!!"
#     if isim == "Leia":
#         return f"{isim} men sening opangman <3"
#     if isim == "Han":
#         return f"{isim} men sening kuyov akangman $$"
#     if isim == "R2D2":
#         return f"{isim} men sening yordamchingman *(o)*"
# print(eslatma())


#default_mood.py

# def kayfiyat():
#     kun=input("Kayfiyatni kiriting = ")
#     if kun == "happy":
#         return "Today, I am feeling happy"
#     if kun == "sad":
#         return "Today, I am feeling sad"
#     if kun == "":
#         return "Today, I am feeling neutral"
# print(kayfiyat())


# repeating_letters.py

# def dublle():
#     matn=input("Matini kiriting = ")
#     return "".join([dub * 2 for dub in matn])
# print(dublle())


# incorrect_import_statement.py

# def im():
#     matn=input("matn = ")
#     qisim = matn.split()
#     return f"from {qisim[-1]} import {qisim[1]}"
# print(im())


#  emphasise_words.py

def katta_harif():
    matn=input("matn = ")
    sozlar = matn.split()
    natija = []
    for soz in sozlar:
        if len(soz) > 0:
            natija.append(soz[0].upper() + soz[1:].lower())
    # print(natija)
    return " ".join(natija)
print(katta_harif())