a=[]
count=0
e=int(input("Enter the array size :"))
print('Enter elements :')
for i in range(e):
    a.append(int(input()))
print('Entered array is ',a)
for i in range(e):
      if a[i]!=0:
           a[count]=a[i]
           count+=1
while count<e:
    a[count]=0
    count+=1
print('Array is :',a)