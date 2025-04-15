# Create a function that takes two strings as arguments and returns either true or false depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
a=input()
b=input()
def sc(a,b):
    if len(a)==len(b):
        return True
    else:
        return False
print(sc(a,b))