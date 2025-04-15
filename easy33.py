# Count occurrence of number: Input: [1,6,3,1,5,9,7,2,1,9,3,7,8,9,10] , no find=7 Output: 7 present 2 times.
list1=list(map(int,input().split()))
f=int(input())
c=0
for i in list1:
    if i==f:
        c+=1
print(f"{f} present {c} times")