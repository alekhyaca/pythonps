# Create a function that takes an array of integers as an argument and returns a unique number from that array. All numbers except unique ones have the same number of occurrences in the array. Example: findSingleNumber([2, 2, 2, 3, 4, 4, 4]) ➞ 3
list1=[2, 2, 2, 3, 4, 4, 4]
def unique(list1):
    list2=[]
    for i in range(len(list1)):
        flag=True
        for j in range(len(list1)):
            if i!=j and list1[i]==list1[j]:
                flag=False
                break
        if flag:
            list2.append(list1[i])
    return list2
print(unique(list1))