'''
a normal divider program that take a no. from user and then take a range as minimum and maximum no.
after that it divide the no. with the range set by you and check if the no. is divisor or not

'''

Apple=int(input('Enter the no. of apple you want to distribute to students : '))
print('\nset range')
mn=int(input('Enter minimum no. : '))
mx=int(input('Enter maximum no. : '))
if mn<mx:
    for i in range(mn,mx):

        if Apple%i==0:
            print(f'{Apple} apples divided between {i} students then each student get {Apple//i} no. of apple')
        else:
            print(f"{Apple} apples can't be equally divided between {i} students add/remove apples first for equall distribution")

else:
    print("maximum no. can't be equal to or lesser than minimum no." )