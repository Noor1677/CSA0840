n=float(input("enter the year"))
if(n==0):
    print("the year is invalid")
elif(n%4==0):
    print("the year is leap")
else:
    print("it is not a leap year")
