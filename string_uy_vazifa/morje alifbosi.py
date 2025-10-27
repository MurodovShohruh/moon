def m():
    a= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    b= ['1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111', '10000', '10001', '10010', '10011', '10100', '10101', '10110', '10111', '11000', '11001', '11010']
    
    matn = input("matini kiriting = ").upper()
    shifr = dict(zip(a,b))
    matinlar = dict(zip(b,a))

    if all(x.isalpha() or x.isspace() for x in matn):
        natija=[]
        for harf in matn:
            if harf in shifr:    
                natija.append(shifr[harf])
            elif harf == " ":
                natija.append("/")
        return " ".join(natija)
        
    else:
        soz = matn.split()
        natija = []
        for kod in soz:
            if kod in matinlar:
                natija.append(matinlar[kod])
            elif kod == "/":
                natija.append(" ")
        return "".join(natija).capitalize()
    
print(m())