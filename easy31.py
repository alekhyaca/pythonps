#  program to insert  the elements of an array for specific index. Input: [1,2,3,4,5,7,8,9,10] , index=5 Output: [1,2,3,4,5,6,7,8,9,10]
list1=list(map(int,input().split()))
list2=[]
element=int(input())
index=int(input())
for i in range(len(list1) + 1):
    if i < index:
        list2.append(list1[i])
    elif i == index:
        list2.append(element)
    else:
        list2.append(list1[i - 1])
print(list2)