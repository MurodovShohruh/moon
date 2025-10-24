def s():
    student={
        "SHOHRUH" : "MURODOV",
        "UMID" : "ABDULAYEV",
        }
    
    for name, sn in student.items():
        print(name)
        print(sn)
    return student
print(s())