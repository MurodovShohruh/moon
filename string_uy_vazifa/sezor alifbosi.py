def m():
    a= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    c= ['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

    tanlov = input("Tanlovingizni kiriting (1 yoki 2): ")
    matn = input("matini kiriting = ").upper()

    shifr = dict(zip(a,c))
    reshifr = dict(zip(c,a))

    if tanlov == "1":
        natija=[]
        for harf in matn:
            if harf in shifr:
                natija.append(shifr[harf])
            elif harf == " ":
                natija.append("/")
        return "".join(natija)

    elif tanlov == "2":
        natija= []
        for harf in matn :
            if harf in reshifr:
                natija.append(reshifr[harf])
            elif harf == "/":
                natija.append(" ")
        return "".join(natija).capitalize()
    
    else:
        return "Xato tanlov !"

print(m())
