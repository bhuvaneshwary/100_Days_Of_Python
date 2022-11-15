'''

Write a program to take an integer "a" as an input and check whether it ends with 4 or 8. 
if its ends with 4, print "ends with 4", 
if it end with 8, print "ends with 8", otherwise print "ends with neither".
'''

a = int(input("Enter a number = "))
if a % 10 == 4 :
    print(a,"end with 4")
elif a% 10 == 8 :
    print(a,"end with 8 ")
else :
    print(a,"end with neither ")

