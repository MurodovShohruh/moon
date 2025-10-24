def s():
    student={
        "SHOHRUH" : "MURODOV",
        "UMID" : "ABDULAYEV",
        "all age" : 22
        }
    
    for name, sn in student.items():
        print(name, "->", sn)
    return student
print(s())