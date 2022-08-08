
# hope to get 5 score
def UserChoise():
    print("                               enter your choice\n")
    print("1: cube number up to the total value 1000\n2: Get first prime number up to 100\n3: user age classification\n4: exit from program")
    UserChoise1 = int(input())
    if UserChoise1 == 1:
        Cube()
    elif UserChoise1 == 2:
        PrimeNumber()
    elif UserChoise1 == 3:
        Age()
    elif UserChoise1 == 4:
        quit() 
    else:
        print("please enter correct option")
        UserChoise()

        
        



#Cube Number Test... Print out all cubed numbers up to the total value 1000, so if the cubed number is over 1000 break the loop
def Cube():
    x = 1
    for CubeNumber in range(1,100):

        result = CubeNumber * CubeNumber * CubeNumber      # or we can do CubeNumber ** 3 rather then typing 3 time cubes
        if result > 1000:
            break

        else:
            print(result)
    UserChoise()


#Cube()

#Get first prime numbers up to 100
def PrimeNumber():            
       
    for i in range(1,101):
        counter = 0                                     
        for j in range(1,i+1):                  
            if (i % j == 0): 
                counter = counter + 1
        if counter == 2:   
            print(i)
    UserChoise()
#PrimeNumber()


#Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors


def Age():
    UserAge = int(input("enter your age: "))
    if UserAge < 18:
        print("Kids")
    elif (UserAge >=18) and (UserAge <= 65):
        print("Adults")

    else:
        print("senior")
    UserChoise()

#Age()

UserChoise()
        



