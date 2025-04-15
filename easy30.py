# Program to count vowels and consonants in a given String. Input: i am ram Output: 3 vowels 3 consonants.
str=input()
vowels="aeiouAEIOU"
vc=0
cc=0
for i in str:
    if i not in vowels and i!=" ":
        cc+=1
    elif i in vowels:
        vc+=1
print(f"{vc} vowels {cc} consonants")