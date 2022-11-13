temp =  float(input("Enter the temperature in celsius please"))
if temp < -273.15 :
    print("The temperature is zero")
elif  temp == -273.15 :
    print("the temperaure is absolute zero")
elif 0<temp <-273.15 :
    print("The temperature is below freezing point")
elif 0<temp<100 :
    print("The temperature is in the normal range")
elif temp == 100 :
    print("The temperature is at boiling point")
else : 
    print("The temperature is above the boiling point")