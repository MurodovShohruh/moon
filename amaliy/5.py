num=int(input(" son= "))
n=[]
i=0
while i<=num:
    if num>0:
        num=int(input(" son= "))
        i*=i
        n.append(num)
    elif num==0:
        print("umumiy yig'indi",sum(n))
        break