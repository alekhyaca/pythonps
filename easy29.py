# Program to find a missing number Input:  n=5(length of array), arr= [5,3,1,4] Output: 2 is missing Using loop only(you can not use predefined function)
n=int(input())
arr=list(map(int,input().split()))
for i in range(1,n+1):
    if i not in arr:
        print(f"{i} is missing")