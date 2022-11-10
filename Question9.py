n = int(input("user please enter a number "))
print(type(n))
#method 1 

square_num = n**2
cube_num = n**3 
print(square_num)
print(cube_num)

#method 2 
new_square_n =  pow(n,2)
new_cube_n = pow(n,3)
print("he square and cube using the POW function is : ",new_square_n,new_cube_n)