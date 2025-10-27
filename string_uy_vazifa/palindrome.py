def a():
    matn = input("so'zni kiriting = ")
    if matn == matn[::-1] and matn == " ":
        return f"{matn} -> palindrom"
    else:
        return f"{matn} -> not palindrom"
print(a())
