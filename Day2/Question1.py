#A program to obtain principal amount, rate of interest and time and then calculatesimple interest 
P = int(input("Enter the principal amount"))
R = int(input("Enter the rate of interest"))
T = int(input("Enter the time"))
simple_interest = (P*R*T) / 100
print("The final simple interest is :", simple_interest)