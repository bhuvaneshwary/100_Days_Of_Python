#according to the question 
a  = 5
b,c,d,e,f = 1,2,3,4,5 
print(a*b,a*c,a*d,a*e,a*f)

#a more efficient way 
for i in range(1,6):
    product = a*i
    print(product)