'''
print the following - 
*   
**  
* *
*  *
* *
**  
*  
'''

for i in range(7):
      for j in range(4):
            if i == j or j == 6-i :
                        print("*" , end="")
            else :
                   if j == 0 :
                        print("*" , end = "")
                   else :
                        print(" ",end="")
      print()