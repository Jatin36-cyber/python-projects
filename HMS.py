#health management system
#this is a project code of health management system which takes input from user to know that what type of data
# user want as list of user and after selecting user which plan they want to see as workout plan or meal plan


n=int(input('type 1 to show list and type 2 to select from list'))
for o in range(2):
    if n==1:
        q=int(input('1 for harry,2 for marry,3 for guddu'))

        if q==1:
            w=int(input('1. for meal and 2. for workout plan'))
            if w==1:
                print('weight loss meal')
                break
            else:
                print('pushups')
                break
        elif q == 2:
            w = int(input('1 for meal and 2 for workout'))
            if w == 1:
                print('weight gain meal')
                break
            else:
                print('squats')
                break
        elif q == 3:
            w = int(input('1 for meal and 2 for workout'))
            if w == 1:
                print('balance meal')
                break

            else:
                print('biceps curls')
                break
        else:
            print('wrong input')
    elif n==2:
        q = int(input('1 for harry,2 for marry,3 for guddu'))
        if q==1:
            w=int(input('1 for meal and 2 for workout'))
            if w==1:
                print('weight loss meal')
                break
            else:
                print('pushups')
                break
        elif q == 2:
            w = int(input('1 for meal and 2 for workout'))
            if w == 1:
                print('weight gain meal')
                break
            else:
                print('squats')
                break
        elif q == 3:
            w = int(input('1 for meal and 2 for workout'))
            if w == 1:
                print('balance meal')
                break

            else:
                print('hammer curls')
                break
        else:
            print('wrong input')
    else:
        print('wrong input')

