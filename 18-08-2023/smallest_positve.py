def findNum(arr,n):

    for i in range(1,n+1):
        flag=False
        for j in range(n-1):
            if arr[j]==i:
                flag=True
                break
        if flag==False:
            return i
arr=[-2,1,3,10]
length=len(arr)
res=findNum(arr,length)
print("The smallest positive missing number is :",res)
