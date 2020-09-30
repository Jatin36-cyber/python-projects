#this project code is for gussing the no. by the user
#if user gusse big no. from the original no. then message displayed is (choose small no.)
#if user gusse small no. from the original no. then message displayed is (choose large no.)
#if user gusses same no. that is equal to the original no. then message displayed is (right)

n=18
for i in range(4):
    w=int(input())


    if w>n:
        print('choose small no.')
    elif w==n:
        print('right')
        break
    else:
        print('choose big no.')
