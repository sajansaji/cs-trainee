arr = [20,32,15,100,65]
n=5
print('Peak elements are :')
for i in range(n):
    if(arr[i-1]<arr[i] and arr[i]>arr[i+1]):
        print(arr[i])