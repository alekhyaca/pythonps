# Program to find LCM of two numbers using while loop Input: 15 50  Output: Lcm of 15 and 50 is 150.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)
print(lcm(15,50))