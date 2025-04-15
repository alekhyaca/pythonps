# Create a function that returns an array of strings sorted by length in ascending order. Example: sortByLength(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
list1=["a", "ccc", "dddd", "bb"]
def sbl(list1):
    n=len(list1)
    for i in range(n):
        for j in range(0,n-i-1):
            if len(list1[j])>len(list1[j+1]):
                list1[j],list1[j+1]=list1[j+1],list1[j]
    return list1
print(sbl(list1))