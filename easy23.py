# C Program to arrange numbers in ascending order Input: [2,3,1,5,4] Output: [1,2,3,4,5] Sort the Array using loop only(you can not use predefined function).
list1=[2,3,1,5,4]
def asc(list1):
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]>list1[j]:
                list1[i],list1[j]=list1[j],list1[i]
    return list1
print(asc(list1))