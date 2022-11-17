'''

Q6. Write a program that should prompt the user to type some sentence (s) followed by “enter”. 
It should then print the original sentence (s) and the following statistics
relating  to sentence (s):
(1) number of word
(2) number of character (including  white space and punctuation )
(3) percentage of character that are alpha numeric

'''

sentence = input("Enter a sentence = ")
count = 1
alphabet = 0 
for j in sentence :
    if j == " " :
        count += 1
    elif j.isalnum() :
        alphabet += 1
        
print("Number of word is ",count)
print("Number of characters ",len(sentence))
print("Percentage of alpha numeric = ", (alphabet / len(sentence)) * 100)