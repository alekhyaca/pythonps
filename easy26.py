# Program to Check Whether a Number is Prime or Not Input: 9 Output: 9 is not a prime no Input: 7 Output : 7 is a prime no
n=int(input())
def prime(n):
    flag=True
    for i in range(2,n):
        if n%i==0:
            flag=False
            break
    if flag:
        return f"{n} is a prime no"
    else:
        return f"{n} is not a prime no"
print(prime(n)) 