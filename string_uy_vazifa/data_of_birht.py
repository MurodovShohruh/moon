def c():
    numbers = input("Tug‘ilgan kuning, oying, yilingni kiriting: ")
    raqamlar = numbers.split() 
    jami = 0

    for num in raqamlar:
        for raqam in num: 
            jami += int(raqam)

    while jami > 9:
        z = 0
        for r in str(jami):
            z += int(r)
        jami = z

    return f"Hayot raqamingiz: {jami}"

print(c())
