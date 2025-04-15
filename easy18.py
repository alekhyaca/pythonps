# Given a string, create a function to reverse the case. All lower-cased letters should be upper-cased, and vice versa. Example: reverseCase("Happy Birthday") ➞ "hAPPY bIRTHDAY"
def reverseCase(s):
    result = ''
    for char in s:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result
print(reverseCase("Happy Birthday"))