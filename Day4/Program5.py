Farenheit =  0
Celsius = 0
temp_input = int(input("Please enter the value you want to convert"))
temp_con_unit =  str(input("do you want to convert it to celsius or farenheit enter c or f respectively"))
if temp_con_unit == 'f':
    Farenheit = (9/5*temp_input)+32
    print("The value of the temperature in farenheit is :" ,  Farenheit)
else :
    Celsius  = 5/9**(temp_input*32)
    print("The value of the temperature in celsius is :" ,  Celsius)