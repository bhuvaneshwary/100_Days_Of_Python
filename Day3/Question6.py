a =  int(input("Please enter the first side " ))
b =  int(input("Please enter the second side " ))
c =  int(input("Please enter the third side " ))
if a+b >c and b+c > a and c+a>b :
    print("it can form a triangle")
else:
    print("it cannot form a triangle")