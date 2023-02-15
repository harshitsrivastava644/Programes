#Program to generate prime numbers till given input number
def isPrime(n):
    if (n==1 or n==0):
        return False
    for i in range(2,(n//2)+1):
        if(n%i==0):
            return False
    return True

n = int(input("Enter number"))
for i in range(1,n+1):
    if(isPrime(i)):
        print(i,end="  ")
