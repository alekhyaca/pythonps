# Program to Display Characters from A to Z Using Loop with count. Output: A1 B2 C3 D4 E5 F6 ……. Z26
for i in range(26):
    char = chr(ord('A') + i)   
    count = i + 1              
    print(f"{char}{count}", end=" ")