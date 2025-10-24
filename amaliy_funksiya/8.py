def s():
    student={
        "SHOHRUH" : "MURODOV",
        "UMID" : "ABDULAYEV",
        "garde": "A"
        }
    
    for name, sn in student.items():
        print(name, "->", sn)
    return student
print(s())