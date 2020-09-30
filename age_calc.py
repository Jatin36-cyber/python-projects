'''
-this programme is to check different task related to age of the user you can check when you turn 100
or how many years old are you at specific year.

'''
def age_calculator(x):
    while True:
    #continuos loop
        if x>0 and x<150:
        #if user enter no. between 0 to 150 this consider as age
            print(f'you enter your age that is {x} years old')
            print('what you want to calculate:\n1.) your age at specific year\n2.) when you turn 100 years old\n3.) your year of birth')
            y=int(input('choose from above options as 1, 2 or 3 : '))
            if y==1:
                z=int(input('enter year no. : '))
                if z>=(2020-x):
                    q=x+(z-2020)
                    print(f'you are {q} years old on {z}')
                else:
                    print(f'you are not born in {z}')
            elif y==2:
                if x<100:
                    w=(100-x)+(2020)
                    print(f'you turn 100 after {100-x} years and in year {w}')
                else:
                    print('you are older than 100 years old')
            elif y==3:
                e=2020-x
                print(f'your year of birth is {e}')

            else:
                print('wrong options type only 1 2 or 3')
        elif x>1700 and x<2020:
        #if user enter no. between 1700 to 2020 this consider as year of birth
            print(f'you enter your year_of_birth that is {x}')
            print('what you want to calculate:\n1.) your age at specific year\n2.) when you turn 100 years old\n3.) your age now')
            y = int(input('choose from above options as 1, 2 or 3'))
            if y == 1:
                z = int(input('enter year no. : '))
                if z>=x:
                    q = z-x
                    print(f'you are {q} years old on {z}')
                else:
                    print(f'you are not born in {z}')
            elif y == 2:
                a=2020-x
                if a < 100:
                    w = (100 - a) + (2020)
                    print(f'you turn 100 after {100 - a} years and in year {w}')
                else:
                    print('you are older than 100 years old')
            elif y == 3:
                e = 2020 - x
                print(f'your age is {e}')

            else:
                print('wrong options type only 1 2 or 3')

        else:
            print(f'it is not possible that you are {x} years old or born in year {x}\nplease enter the exact year of birth or your age ')

            break
        print('\n\n')



if __name__ == "__main__":
    x=int(input("Enter Your Year_of_Birth or your age : "))
    age_calculator(x)