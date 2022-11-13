side_1 =  int(input("Please enter the first side " ))
side_2 =  int(input("Please enter the second side " ))
side_3 =  int(input("Please enter the third side " ))
if side_1==side_2==side_3 : 
    print("It is an equilateral triangle")
elif side_1 == side_2 != side_3 or side_1 != side_2 == side_3 or side_1 == side_3 != side_2 :
    print("it is an isoceles triangle")
else :
    print("it is a scalene triangle")