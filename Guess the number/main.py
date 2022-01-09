import random 
randnumber = random.randint(1, 100)

userguess = None
guesses = 0

while(userguess != randnumber):
     userguess = int(input("enter your guess:\n"))
     guesses +=1
     if(userguess==randnumber):
        print("you guesses it right")
     else:
         if(userguess>randnumber):
          print("you guessed it wrong enter a smaller number") 
         else:
             print("you guessed it wrong enter a a larger number")

print(f"you guessesd the number in {guesses} guesses")
with open("hiscore.txt" , "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("you have just broken the high score")
with open("hiscore.txt", "w") as f:
    f.write(str(guesses))