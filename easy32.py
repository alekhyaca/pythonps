# Reverse a number using while Loop Input: 123 Output: 321
num=int(input())
num1=0
while num!=0:
    d=num%10
    num1=num1*10+d
    num//=10
print(num1)