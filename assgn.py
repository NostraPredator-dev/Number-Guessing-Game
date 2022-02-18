import random

print ("Number Guessing Game")
print ("Guess a number between 1-9")

num = random.randint(1,10)
gss = 0
for x in range(1,6):
    gss = int(input("Guess a number : "))
    if num == gss:  
        print("Congratulations YOU WIN !!!")
        exit()
    else:
        if (num > gss):
            print("Guess a number higher than",gss)
        else:
            print("Guess a number less than",gss)
if gss != num:
    print("YOU LOSE. Try Again")