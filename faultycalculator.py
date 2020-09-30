#this is a faulty calculator program which takes input from user and print the correct result but if the user
# want these 3 calculation (55*2=24     45*4=23     23*0=2) then result is wrong as given.

for i in range(19):

    a=int(input('enter first no.'))
    d=input('enter operator')
    b=int(input('enter 2nd no.'))

    print('your ans =',end="")

    if d=='+':
        print(a+b)
    elif d=='*':
        if a*b==110:
            print(24)
        elif a*b==180:
            print(23)
        elif a*b==0:
            print(2)
        else:
            print(a*b)
    elif d=='-':
        print(a-b)
    elif d=='/':
        print(a/b)
    else:
        print('wrong')

    print('\n')