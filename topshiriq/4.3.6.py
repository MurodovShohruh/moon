oy1=[31,28,31,30,31,30,31,31,30,31,30,31]
oy2=[31,29,31,30,31,30,31,31,30,31,30,31]
kun=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
oy=["Yanvar","Febral","Mart","Aprel","May","Iyun","Iyul","Avgust","Sentyabr","Oktiyabr","Nayabr","Dekabr"]
def number(Y,O,K):
    if Y*365%2==0:
        return Y,"kabisa yili"  ,kun [K-1],oy [O-1],oy2 [O-1],"kundan iborat"
    elif Y*365%2!=0:
        return Y, "yil" ,kun [K-1],oy [O-1],oy1 [O-1],"kundan iborat"
print(number(456724,5,7))