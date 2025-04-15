# Create a function that takes an array of arrays with numbers. Return a new (single) array with the largest numbers of each. Example: findLargestNums([[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0]]) ➞ [7, 90, 2]
list1=[[4, 2, 7, 1], [20, 70, 40, 90], [1, 2, 0],[2,7,99]]
list2=[]
def fl(arrays):
    for sub_array in arrays:
        l=sub_array[0]
        for  i in sub_array[1:]:
            if i>l:
                l=i
        list2.append(l)
    return list2
print(fl(list1))