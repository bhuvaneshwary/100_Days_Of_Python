'''
Q. Write a program that reads from user -
-----> An hour between 1 to 12 and
-----> Number of hours ahead. The program should then print the time after those many hours.

'''


hour = int(input("Enter An hour between 1 to 12 :-"))
hours_left = int(input("Enter Number of hours ahead :-"))
sum_hours = hour + hours_left
if sum_hours  <= 12 :
    print("Time is ",sum_hours ,"o clock")
else :
    print("Time is ",sum_hours  - 12,"o clock")