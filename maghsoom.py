a=int(input("enter a  number:"))
b=int(input("inter an other number:"))

print("maghsoomalayhaymoshtarak:)")
for i in range(1,b+1):
    if (b % i == 0 and a%i==0):
        print(i)
