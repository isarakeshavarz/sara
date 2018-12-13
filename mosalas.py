import math
x1=int(input("x1:"))
y1=int(input("y1:"))
x2=int(input("x2:"))
y2=int(input("y2:"))
x3=int(input("x3:"))
y3=int(input("y3:"))
a1=math.sqrt((x1-x2)**2+(y1-y2)**2)
a2=math.sqrt((x2-x3)**2+(y2-y3)**2)
a3=math.sqrt((x3-x1)**2+(y3-y1)**2)
a=a1+a2+a3
print("mohit:",a)
b=x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)
if b<0 :
    b=-1*b
print("masahat:",b)
