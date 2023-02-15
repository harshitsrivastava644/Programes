#to check if the input number is prime or not
num = int(input("Enter a number:"))
A = False
if num > 1:
    for i in range(2,num):
        if (num%i) == 0:
            A = True
            break
if A:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")
