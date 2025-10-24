name = input("isimni kiriting: ")
names= {name:"Ali", name:"Bobur"}
if name in names:
    print(f"bu isim royxarda bor", {name})
elif name not in names:
    print(f"bu isim royxatda mavjut emas", "ERROR" , {name} )