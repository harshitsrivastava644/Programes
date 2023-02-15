#Python program to remove first occurance of a character in a string
str1 = input("Enter a string:")
char = input("Enter a character:")
string2=" "
length = len(str1)
i=0
while(i<length):
    if(str1[i]==char):
        str2 = str1[0:i] + str1[i+1:length]
        break
    i = i+1

print("Original string:",str1)
print("final string:",str2)