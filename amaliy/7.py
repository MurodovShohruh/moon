try:
    a=int(input("1-son= "))
    b=int(input("2-son= "))
    print(a//b)
except ZeroDivisionError:
    print("Nolga bo'linmaydi!!")
    