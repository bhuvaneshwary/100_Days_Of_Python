no_of_items = int(input("Please enter the number of items you bought "))
if no_of_items < 10 :
    print("the total cost you would have to pay is :" ,  no_of_items*120)
if 10<no_of_items<99 :
    print("the total cost you would have to pay is :" , no_of_items*100)
else:
     print("the total cost you would have to pay is :" , no_of_items*70)