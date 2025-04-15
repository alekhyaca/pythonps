# C Program to Calculate the Power of a Number(using loop only).Input: n=5, p=3 Output: 5 ^ 3 = 125 Explanation: 5 x 5 x 5 = 125
n=int(input())
p=int(input())
def pon(n,p):
    m=1
    while p!=0:
        m*=n
        p-=1
    return m
print(pon(n,p))       