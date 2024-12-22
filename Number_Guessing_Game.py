import random

print("Welcome to the number guessing game.")
print("You have 7 chances and you have to guess a number from 1 to 100.")
print("-------------------------------------------------------------------")
def userinput():
    x=int(input("Enter your Guess : "))
    if(x<0 or x>100):
        print("Number should be 0 to 100")
        print("-------------------------------------------------------------------")
        return userinput()
    return x
chance=7
number=random.randrange(100)
while(chance):
    n=userinput()
    if(number>n):
        print(n,"is Lesser.")
        chance-=1
        print("You have",chance,"chance left.")
        print("-------------------------------------------------------------------")
    elif(number<n):
        print(n,"is Greater.")
        chance-=1
        print("You have",chance,"chance left.")
        print("-------------------------------------------------------------------")
    else:
        chance-=1
        print("Congratulation! You guessed the right number in",(7-chance),"chances.")
        print("-------------------------------------------------------------------")
        break
input("Press Enter to Exit...")
