# fix_spacing.py

# def tru():
#     x=input("matn = ")
#     ajrat=x.split()
#     return " ".join(ajrat)
# print(tru())


#  has_digit_regex.py

# import re
# def x(s):
#     return bool(re.search(r'\d', s))
# print(x("23cc4"))


#  get_type_value.py

# def typ(x):
#     return type(x)
# print(typ(7))


#  shhh_be_quiet.py

# def m():
#     x=input("matn = ")
#     map=x.capitalize()
#     return map
# print(m())


# verbed_nouns.py

def verbify(a):
    x = a.split()

    soz = x[0]
    if soz.endswith("ed"):
        return a
    else:
        x[0] = soz + "ed"
        return " ".join(x)
print(verbify("shredded cheese"))

