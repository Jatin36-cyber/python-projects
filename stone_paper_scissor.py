#this is a stone paper scissor game which have 3 rounds between user and computer.
#after completition of every round winner name is displayed.
#and after completition of all rounds winner displayed according to the no. of wins

import random
c=0
j=0
for i in range(3):
    jatin=int(input('1 for stone, 2 for paper, 3 for scissor'))
    lst=(1,2,3)
    comp=random.choice(lst)

    print('jatin and comp=' ,jatin,comp)

    if jatin==1 and comp==2:
        print('comp wins')
        c+=1
    elif jatin==1 and comp==3:
        print('jatin wins')
        j+=1
    elif jatin==1 and comp==1:
        print('draw')

    elif jatin == 2 and comp == 1:
        print('jatin wins')
        j += 1
    elif jatin==2 and comp==2:
        print(' draw')
    elif jatin==2 and comp==3:
        print('comp wins')
        c += 1

    elif jatin == 3 and comp == 1:
        print('comp wins')
        c += 1
    elif jatin==3 and comp==2:
        print('jatin wins')
        j += 1
    elif jatin==3 and comp==3:
        print('draw')

    else:
        print('wrong input')



if c>j:
    print(c,'comp wins')
elif c==j:
    print('draw')
else:
    print(j,'jatin wins')
