'''
Write a python script that ask the user to enter a length in centimeters .
if the user  enters a negative length , 
the program should tell  the user that  the entry is invalid . 
otherwise ,the program should convert the length to inches and print out the result .
there are 2.54  centimeters in an inch.
'''
user_len = int(input("enter the length in cms"))
if user_len < 0 :
    print("entry is invalid")
else :
    print("The value of ", user_len,"cms in inches is",user_len/2.54)