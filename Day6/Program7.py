'''

Write a program to accept the age of an employees and 
count the number of person in the following age group.
(a) 26-35
(b) 36-45
(c) 46-55
'''

age = 0
bage = 0
cage = 0
while True :
    employee = int(input("Enter the age of employees (enter 0 (zero) for quit )= "))
    if employee == 0 :
        break
    else :
        if 25 < employee and employee  < 36 :
            a = a + 1
        if 35 < employee and employee < 46 :
            b = b + 1
        if 45 < employee and employee  < 56 :
            c = c + 1
print("the age of employees 26 - 35 = ", age)
print("the age of employees 36 - 45 = ", bage)
print("the age of employees 46 - 55 = ", cage)