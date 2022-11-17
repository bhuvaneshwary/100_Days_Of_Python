'''
Q7. Write a python program as per specifications given below:
(1) repeatedly prompt for  a sentence (string) or for “q” to quit .
(2) upon input of a sentence s, 
print  the string produced  form s by converting each lower case letter to upper case and 
each upper case letter to lower case
(3) all other character  are left unchanged



'''

while True :
    sentence = input("Enter a sentence (for quit enter q or Q)= ")
    if sentence == "Q" or sentence=="q" :
        break
    else :
        for i in range(len (sentence)) :
            if  sentence[i].isupper() :
                print (sentence[i] .lower() , end="" )
            elif sentence[i].islower() :
                print (sentence[i] .upper() , end="" )
            else :
                print(sentence[i] , end="")
        print()
