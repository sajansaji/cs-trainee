r=int(input("Enter the no of rows :"))
c=int(input("Enter the no of columns :"))
m=[]
print("Enter the values of matrix :")
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    m.append(a)
for i in range(r):
    for j in range(c):
        print(m[i][j],end=" ")
    print()
print('Diagonal elements are :')
for i in range(r):
    for j in range(c):
        if i == j:
            print(m[i][j],end=' ')
print('\nlower bound elements are :')
for i in range(r):
    for j in range(c):
        if i > j:
            print(m[i][j],end=' ')
print('\nUpper bound elements are :')
for i in range(r):
    for j in range(c):
         if i < j:
            print(m[i][j], end=' ')