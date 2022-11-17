'''

Write a program which replaces all vowels in the string with '*'.


'''
Str = input("Enter a string :-")
new_string = ""
for i in Str :
    if i == "a"or i == "e"or i == "i"or i == "o"or i == "u"or i == "A"or i == "E"or i == "I"or i == "O"or i == "U":
        new_string += "*"
    else :
        new_string += i
print(new_string)
