#this project code takes input from user to get the no. of rows and another input which is integer for
# different types of * pattern to print

n=int(input('enter new no.'))
ace=int(input('enter boolean value'))

if ace==1:
    for i in range(1,n+1):
        for l in range(i):
            print('x', end="")
        print()

elif ace==0:
    for i in range(n):
        for l in range(n-i):
            print('x',end="")
        print()

else:
    print('choose boolean value 1 or 0')