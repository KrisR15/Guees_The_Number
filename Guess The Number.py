from random import randint

print("The aim of the game is to guess the randomly generated number that is between 1 and 1000.")

target = randint(1,1001)
guess = int(input("What is your first guess? \n \n"))
guess_list=[]

guess_list.append(guess)

while True:
    if guess < 0:
        print("\nOut of Bounds!")
        guess = int(input("\nPlease guess a number between 1 and 100. What is your next guess? \n \n "))
        guess_list.append(guess)
        continue
    elif guess > 100:
        print("\nOut of Bounds!")
        guess = int(input("\nPlease guess a number between 1 and 100. What is your next guess? \n \n "))
        guess_list.append(guess)
        continue
    elif guess == target:
        print("\nCORRECT! WELL DONE!")
        number_of_guesses = len(guess_list)
        print(f"\nNumber of attempts: {number_of_guesses}")
        print(f"\nList of attempts: {guess_list}")
    elif guess >= (target + 10):
        print("\nCOLD!")
        guess = int(input("\nWhat is your next guess? \n \n "))
        guess_list.append(guess)
        break
    elif guess <= (target - 10):
        print("\nCOLD!")
        guess = int(input("\nWhat is your next guess? \n \n "))
        guess_list.append(guess)
        break
    elif guess < (target + 10):
        print("\nWARM!")
        guess = int(input("\nWhat is your next guess? \n \n "))
        guess_list.append(guess)
        break
    elif guess > (target - 10):
        print("\nWARM!")
        guess = int(input("\nWhat is your next guess? \n \n "))
        guess_list.append(guess)
        break
        
while True:
    if guess == target:
        print("\nCORRECT! WELL DONE!")
        number_of_guesses = len(guess_list)
        print(f"\nNumber of attempts: {number_of_guesses}")
        print(f"\nList of attempts: {guess_list}")
        break
    elif guess < 0:
        print("\nOut of Bounds!")
        guess = int(input("\nPlease guess a number between 1 and 100. What is your next guess? \n \n "))
        guess_list.append(guess)
        continue
    elif guess > 100:
        print("\nOut of Bounds!")
        guess = int(input("\nPlease guess a number between 1 and 100. What is your next guess? \n \n "))
        guess_list.append(guess)
        continue
    elif abs(target-guess) < abs(target-guess_list[-2]):
        print("\nWARMER!")
        guess = int(input("\nWhat is your next guess? \n \n "))
        guess_list.append(guess)
        continue
    elif abs(target-guess) > abs(target-guess_list[-2]):
        print("\nCOLDER!")
        guess = int(input("\nWhat is your next guess? \n \n "))
        guess_list.append(guess)
        continue
        
