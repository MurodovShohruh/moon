numbers=[1,2,3,4,5,6,7,8,9,10]
toq = [x for x in numbers if x % 2 != 0]
for x in numbers:
    if x % 2 != 0:
        print(f"Toq sonlar = " , x)