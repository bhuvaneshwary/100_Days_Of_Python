'''
Print the following - 

*
**
***
**
*
'''

num =  int(input("enter a number"))
b = num/2+1
for i in range(1,num):
      if i < b :
            print("*" * i )
      else :
            print("*" * (num-i))
print()
