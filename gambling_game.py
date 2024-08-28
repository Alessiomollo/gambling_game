''' write a number guessing game in three ways:
The computer will generate a random number, then you will try to guess it.
The computer will generate a random number, then the computer will try to guess it using linear search.
The computer will generate a random number, then the computer will try to guess it using binary search.
'''

import random


# The player will try to guess the number
# To play this we need to call the guess_random_number function
def guess_random_number(tries, start, stop):
    random_num = random.randint(start, stop)
    user_num = []

    while tries != 0:
        print(f"Remaining tries {tries}")
        user_guess = int(input(f"Please insert a number between {start} and {stop}: "))
       
        if user_guess < start or user_guess > stop:
            print(f"Please insert a number between {start} and {stop}: ")
            
        elif user_guess in user_num:
            print("You already tried this number. Please choose another number.")

        elif user_guess == random_num:
            print(f"You guess the correct number!")
            return
        elif user_guess < random_num:
            print("Guess higher!")
            tries -= 1
        else:
            print("Guess lower!")
            tries -= 1
        user_num.append(user_guess)
    print(f"You have failed to guess the number: {random_num}")


# guess_random_number(5,0,10)


# The computer will try to guess the number
# Use of linear search
# To play this we need to call the guess_random_num_linear function
def guess_random_num_linear(tries, start, stop):
    random_num = random.randint(start, stop)
    print(f"The number for the program to guess is: {random_num}")
    for number in range(start, stop + 1):
        if tries == 0:
            print("The program has failed to guess the correct number!")
            return False
        print(f"Number of tries left: {tries}")
        print(f"The program is guessing... {number}")
        
        
        
        if number == random_num:
            print("The program has guessed the correct number!")
            return True
        tries -= 1


# guess_random_num_linear(5,0,10)


# The computer will try to guess the number
# Use of binary search
# To play this we need to call the guess_random_num_binary function
def guess_random_num_binary(tries, start, stop):
    random_num = random.randint(start, stop)
    print(f"Random number to find: {random_num}")
    low_num = start
    high_num = stop
    pivot = (low_num + high_num) // 2
    while tries != 0:
        if pivot == random_num:
            print(f"Found it! {random_num}")
            return
        elif pivot > random_num:
            high_num = pivot -1 
            print("Guess lower!")

        else:
            low_num = pivot +1
            print("Guess higher!")
        tries -= 1
    print("You program failed to find the number!")

# guess_random_num_binary(5,0,100)



# Create a function that lets the user decide which of the 3 previous functions want to use
def user_decision():
    
    while True:
        while True:
            try:
                user_tries = int(input("\nPlease insert the number of tries: "))
                if user_tries > 0:
                    break
                else:
                    print("\nPlease insert a positive number.")
            except(ValueError, TypeError, NameError):
                    print("\nPlease insert a positive number.")
        
        while True:
            try:       
                user_start = int(input("Please insert a number to set as a start: "))
                if user_start > 0:
                    break
                else:
                    print("\nPlease insert a positive number.")
            except(ValueError, TypeError, NameError):
                print("\nPlease insert a positive number.")
        
        while True:
            try:
                user_stop =  int(input("\nPlease insert a number to set as a stop: "))
                if user_stop > 0:
                    break
                else:
                    print("\nPlease insert a positive number.")
            except(ValueError, TypeError, NameError):
                print("\nPlease insert a positive number.")
        
        while True:
            print("1. guess_random_number")
            print("2. guess_random_num_linear")
            print("3. guess_random_num_binary")
            try:
                user_game_choice = int(input("Make your choice: "))
                if user_game_choice >= 1 and user_game_choice <= 3:
                    break
                else:
                    print("Please choose between 1, 2 and 3")
            except(ValueError, TypeError, NameError):
                print("Please choose between 1, 2 and 3")

       
        if user_game_choice == 1:
            guess_random_number(user_tries, user_start, user_stop)
            break
        elif user_game_choice == 2:
            guess_random_num_linear(user_tries, user_start, user_stop)
            break        
        else:
            guess_random_num_binary(user_tries, user_start, user_stop)
            break


# user_decision()


# This is the final game where everything is put together.
'''When called, it should ask the player to bet on whether the computer will or will not guess the correct number.
The player starts out with $10 and can bet $1 to $10 max, in integer increments of $1. The player cannot bet more $ than they have.
The program should call the guess_random_num_linear() function with arguments that would produce a 50/50 chance, or near it.
If the player bet correctly, the player doubles their bet. If the player bet incorrectly, the player loses their bet.
If the player runs out of money, the player loses and the game is over.
If the player reaches > $50, the player wins and the game is over.'''

def gambling_game():
    player_money = 10
    while True:
        while True:
            try:
                user_choice = int(input("\nWill the computer guess the correct number?\n1.Yes\n2.No\n3.Exit: "))
                if user_choice == 1:
                    print("\nYou choose Yes")
                    break
                elif user_choice == 2:
                    print("\nYou choose No")
                    break
                elif user_choice == 3:
                    return False
            except(TypeError,ValueError,NameError):
                print("\nPlease type 1, 2 or 3")
            else:
                print("\nPlease type 1, 2 or 3")
        
        print(f"\nYou have: ${player_money}")
        while True:
            try:
                player_bet = int(input(f"Make your bet: "))
                if player_bet <= 10 and player_bet <= player_money:
                    print(f"You bet: ${player_bet}")
                    break
                
            except(ValueError, TypeError, NameError):
                print("\nPlease bet a max of $10")
            else:
                print(f"\nYou have {player_money}.\nPlease choose a different amount with a max of $10!")
        
        print("")
        computer_number = guess_random_num_linear(5,0,10)
        if user_choice == 1 and computer_number == True:
            player_money += player_bet
            print(f"\nYou guessed correctly!\nYou now have: ${player_money}")
            if player_money > 50:
                print(f"\nYou have ${player_money},\nYou WIN!")
                break
        else:
            player_money -= player_bet
            print(f"\nYou guessed incorrectly!\nYou now have: ${player_money}")
            if player_money <= 0:
                print("\nYou don't have enough money.\nYou LOSE")
                break

            
gambling_game()