Principal  = int(input("please enter the principal money you borrowed"))
rate_of_interest =  12
Time  = int(input("please enter the time_duration"))

simple_interest = (Principal*rate_of_interest*Time) / 100
print(simple_interest)
#p * ( (1 + (r / 100 ))** t ) - p 

compound_interest = Principal*((1+(rate_of_interest/100))**Time) - Principal
print(compound_interest)