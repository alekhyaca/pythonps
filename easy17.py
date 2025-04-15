# Create a function that takes a string and returns the number (count) of vowels contained within it. Example: countVowels("Celebration") ➞ 5
vowels="aeiouAEIOU"
def countVowels(str):
    count=0
    for i in str:
        if i in vowels:
            count+=1
    return count
print(countVowels("Celebrations"))