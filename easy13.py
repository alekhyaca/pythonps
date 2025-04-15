# Create a function that takes an array of numbers and returns the second largest number. Example: secondLargest([10, 40, 30, 20, 50]) ➞ 40
list1=[10, 40, 30, 20, 50]
def sl(list1):
    for i in range(len(list1)):
        for j in range(0,len(list1)-i-1):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    return list1[-2]
print(sl(list1))