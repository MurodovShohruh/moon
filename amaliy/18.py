student = {"name1":"Bobur" , "name2":"Amirxon", "name3":"Ziyoda"}
new_student = ["name4","name2"]
for ns in new_student:
    if ns in student:
        print(ns, "->", student[ns])
    else:
        print(ns, "is not in dictionary")