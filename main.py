import random
# let the machine choose a random number
n = random.randint( 1 , 100)

a = -1
guesses = 1 

while(a != n):
    a = int(input("Guess the number between 1 to 100 :"))

    if(a > n):
        print("Guess a lower number")
        guesses+=1

    elif(a<n):
        print("Guess a higher number")
        guesses+=1

print(f"You have guessed the number {a} correctly in {guesses} guesses")