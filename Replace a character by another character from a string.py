#To replace a character in string with another character
str1 = input("Enter your string:")
ch = input("Enter character to get replaced:")
newch = input("Enter new character to replace:")
str2 = " "
for i in range(len(str1)):
    if(str1[i]==ch):
        str2=str2+newch
    else:
        str2=str2+str1[i]
print("\nOriginal string:",str1)
print("Modified string:",str2)