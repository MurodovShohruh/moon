student = {"name1":"Bobur" , "name2":"Amirxon", "name3":"Ziyoda"}
lis=[]
for key,value in student.items():
    lis.append(key)
    lis.append(value)
print(tuple(lis))