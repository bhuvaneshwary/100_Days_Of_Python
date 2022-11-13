answer = str(input("Do you want to run a code that can compute the value of (a+b)^3 ?"))

if answer == "no":
    print("ok.")
else :
       
        a =  int(input("enter the first number please"))
        b = int(input("enter the second number please"))
        pwer = a**3 +b**3 + 3*a**2*b + 3*a*b**2
        print("the value is  - " , pwer)
        