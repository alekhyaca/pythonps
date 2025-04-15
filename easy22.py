# C Program to find factorial of number.Input: n=5 Output: 120 Explanation: 5 x 4 x 3 x 2 x 1 = 120
n=int(input())
def fact(n):
    if n==0 or n==1:
        return 1
    else:  
        return n*(fact(n-1)) 
print(fact(n))