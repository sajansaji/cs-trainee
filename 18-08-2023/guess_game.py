import random
num=random.randint(1,20)
for i in range(5):
    g = int(input("\nEnter your guess : "))
    if(g==num):
        print("You are right.\n")
        break
    elif(g>num):
        print("High.\n")
    else:
        print("low.\n")
    print("\nRemaining guess : ",4-i)
print("Number generated is :",num)
print("😉")
