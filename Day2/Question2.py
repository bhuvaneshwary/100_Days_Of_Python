#A program to obtain he input of temperature on every day of the week and then print the avg temp
avg_temp = 0
for i in range (0,7):
    temp = int(input("Please enter the temperature"))
    avg_temp = avg_temp+temp
weekly_avg = avg_temp/7
print("the weekly avg temp is",weekly_avg)
