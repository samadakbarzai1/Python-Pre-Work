Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the
#function. The first line of the code has been defined as below. 
# def hello_name(user_name):
def hello_name(user_name):
    print("hello_name" + user_name.title()+ "!")
hello_name('username')


#Question 2 
#Write a python function, first_odds that prints the odd numbers from 
#1-100 and returns nothing def first_odds():
def first_odds():
    for first_odds in list(range(1,100,2)):
        print(first_odds)

first_odds()


#Question 3
#Please write a Python function, max_num_in_list to return the max number of a 
# given list. The first line of the code has been defined as below. 
# def max_num_in_list(a_list):
a_list = range(1,200)
def max_num_in_list(a_list):
    print(max(a_list))

max_num_in_list(a_list)


#Question 4 
#Write a function to return if the given year is a leap year. A leap year is 
# divisible by 4, but not divisible by 100 unless it is also divisible by 400. 
# The return should be boolean Type (true/false). def is_leap_year(a_year):
a_year = 2022
def is_leap_year(a_year):
    a_year = 2022
    if (a_year % 400 == 0) or (a_year % 4 == 0 and a_year % 100 != 0): 
        print(True)
        print(str(a_year) + " is a leapyear")
    else:
        print(False)
        print(str(a_year) + " is not a leapyear")
is_leap_year(a_year)


#Question 5
#Write a function to check to see if all numbers in the list are consecutive 
#numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] 
#are not consecutive numbers. The return should be boolean Type. 
#def is_consecutive(a_list):
list_a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list_b = [1,2,3,4,5,6,7,8,9,11,13,15,17,18,19,20]
list_c =[1,12,3,5,16,8,9,12,4]
def is_consecutive(a_list):
    for ind, number in enumerate(a_list):
        if ind == 0:
            continue
        else:
            if a_list[ind] == a_list[ind-1] + 1:
                continue
            else:
                print(False)
                return(True)
                break            
    print(True)


is_consecutive(list_c) 
is_consecutive(list_a)