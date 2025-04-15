# Create a function that takes an array of items, removes all duplicate items and returns a new array in the same sequential order as the old array (minus duplicates).Example: removeDups([1, 0, 1, 0]) ➞ [1, 0], removeDups(["The", "big", "cat"]) ➞ ["The", "big", "cat"]
list2=[]
def rd(list1):
    for i in list1:
        if i not in list2:
            list2.append(i)          
    return list2
print(rd([1,0,1,0]))