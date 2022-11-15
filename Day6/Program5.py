n = int(input("enter a number greater than 20 = "))
for i in range(11,n+1):
    if i % 3 == 0 and i % 7==0 :
        print(i,"tipsytopsy")
    elif i % 3==0  :
        print(i,"tipsy")
    elif  i % 7==0 :
        print(i,"topsy")
        