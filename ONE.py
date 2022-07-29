# question 1:
#  Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):

user_name = input("inter your username:- ")
def hello_name(User_name):
    print(User_name)

hello_name(user_name)

print("======================================================")

# question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds():
    for OddsNumber in range(1, 100, 2):
        print(OddsNumber)

first_odds()

print("==========================================================")


# question 3:
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):


a_list = [] 
a_list = input("enter a list of number to find maximum number of given list(,):- ")
def max_num_in_list(User_List):
    print(max(User_List))

max_num_in_list(a_list)


print("==================================================================")




# question 4:
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. 
# The return should be boolean Type (true/false). def is_leap_year(a_year):

LeapYear = int(input("enter a year to find a leapyear:- "))
def is_leap_year(a_year):
    if (a_year % 400 == 0) or (a_year % 4 == 0 and a_year % 100 != 0): 
        return True 
    else:
        return False
    
result = is_leap_year(LeapYear)
print(result)



print("==================================================================")



# question 5:
# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers,
#  but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):

listA = [1,2,3,4,5,6,7,8]
def is_consecutive(listA):
    SortedList = sorted(listA)
    range_list=list(range(min(listA), max(listA)+1))
    if SortedList == range_list:
        return True 
    else:
        return False 
    
results = is_consecutive(listA)
print(results)



    


