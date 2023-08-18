a=[1,5,1,9,6,9,1,3,4]
size=9
for i in range(size-1):
    for j in range(size):
        if a[i]==a[j]:
            for k in range(size):
                a[k]=int(input(a[k+1]))
                size-=size
                j-=j
for l in range(size):
    print(a)