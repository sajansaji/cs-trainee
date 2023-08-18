c=200
s=10
print("Hi my great customer...\n")
b=int(input('How many pepsi bottles you want ? '))
if s>=b:
    for i in range(b):
        print('Take it :)')
else:
    for j in range(s):
         print('Take it :)')
    print("Available bottles is ", s)

    print('\nOut of stock\n')
print('Enjoy your drink...Happy to serve you\nSee you next time')
