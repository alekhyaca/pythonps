# Create a function that takes two strings as arguments and returns the number of times the first string (the single character) is found in the second string. Example: charCount("c", "Chamber of secrets") ➞ 1
def charCount(char,text):
    count=0
    for c in text:
        if c==char or c.lower==char.lower or c.upper==char.upper:
            count+=1
    return count
print(charCount("c","Chambers of secrets"))