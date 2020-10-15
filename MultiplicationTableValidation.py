import random

def FakeMultiplicationTable(number):#this function create a multiplication table by taking a no. and then
# print the table as a list but the value it takes a random value at which to put wrong multiplied value
# as it is a fake multiplication table
    wrong = random.randint(1, 9) #take random value between 1 to 9
    table = [i * number for i in range(1, 11)] # making a list for multiplication table
    table[wrong] = table[wrong] + random.randint(0, 10) #addind wrong value randomly in list
    return table

def TableValidation(table, number): #this function validate table and if value are wrong than print given error
    for i in range(1,11):
        if table[i-1] != i*number: #check every value and if multiplication is wrong than provide the index of wrong value
            return i

    return None

if __name__ == "__main__":
    number = int(input("Enter a number for which you want to print multiplication table: ")) #taking input from user
    myTable = FakeMultiplicationTable(number) #calling FakeMultiplicationTable function
    print('\n')
    j = 1
    for i in myTable:
        print(f'{number} * {j} = {i}') #printing in table format
        j=j+1
    wrongIndex = TableValidation(myTable, number) #validating table
    print(f"\nERROR:The table is wrong at index {wrongIndex-1} As when you multiply {number} from {wrongIndex} it gives value {number*wrongIndex} and that is not equal to {myTable[wrongIndex-1]}")