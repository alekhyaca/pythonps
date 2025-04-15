# Create a function that takes two arguments. Both arguments are integers, a and b. Return true if one of them is 10 or if their sum is 10.
a=int(input())
b=int(input())
def t(a,b):
    if a==10 or b==10 or a+b==10:
        return True
    else:
        return False
print(t(a,b))