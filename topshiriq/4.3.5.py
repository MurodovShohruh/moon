oy=["Yanvar","Febral","Mart","Aprel","May","Iyun","Iyul","Avgust","Sentyabr","Oktiyabr","Nayabr","Dekabr"]
oy1=[31,28,31,30,31,30,31,31,30,31,30,31]
oy2=[31,29,31,30,31,30,31,31,30,31,30,31]
def number(Y,O):
    if Y*365%2==0:
        return Y,"kabisa yili"  ,oy [O-1],oy2 [O-1],"kundan iborat"
    elif Y*365%2!=0:
        return Y, "yil" ,oy [O-1],oy1 [O-1],"kundan iborat"
print(number(456724,5))