# Program to find greatest of three numbers(using ternery operator). Input:  4 8 2 Output: 8 is gretest
def greatest(a,b,c):
    g=a if (a>b and a>c) else (b if b>c else c)
    return f"{g} is greatest"
print(greatest(4,8,2))
