'''
Write a short program to find average of list of number entered through keyboard.
'''
sum = 0
smth  =  0
while True:
    num = int(input("Please enter a number(if you wanna quit say yes)"))
    if num == "yes" or "YES":
        if smth != 0 :
            print("Average - ", sum/smth)
            break 
        else:
            print("avg is zro")
    else:
        sum =  sum+int(num)
        smth = 0+1