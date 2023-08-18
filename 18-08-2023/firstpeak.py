arr = [200,32,15,100,65]
n=5
print('First peak element is :')
for i in range(n):
    if(arr[i-1]<arr[i] and arr[i]>arr[i+1]):
        print(arr[i])
        break