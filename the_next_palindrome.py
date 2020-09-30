"""
-palindrome is a no. or a string that is if reversed is same as not reversed for eg.
 mom,2112,nitin,909
-this code help us to find next integer palindrome of a no. that is entered by the user
"""

# next_greater_palindrome function increment the no. until it finds the next palindrome
def next_greater_palindrome(num):
    num = num+1
    while not is_palindrome(num):
        num = num+1
    return num
# is_palindrome function convert a given no. to str format and check if given no. is equal when it reversed
def is_palindrome(num):
    return str(num) == str(num)[::-1]


if __name__ == "__main__":
    #user enter how many no. they want to check
    test=int(input('Enter the No. Of test case you want to perform : '))
    number=[]
    for i in range(test):
        #user enter no. they want to find palindrome for
        num=input('Enter you no. : ')
        try:
            #try to convert input into string
            a=int(num)
            #after converting append into list
            number.append(a)
        except:
            #if unable to convert into int
            print("value you entered is not an integer please enter integer value only\n\n")

    for i in range(len(number)):
        print("\npalindrome sequences")
        print(f'next palindrome of no. {number[i]} is {next_greater_palindrome(number[i])}')

