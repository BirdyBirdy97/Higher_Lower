from art import logo, vs
from game_data import data
from replit import clear
import random

#Functions
def definer():
    """Randomly choosing from the list of people and returning their info statement to be printed later."""
    choice = random.choice(data)
    return choice

def speech(choice):
    """Returns the statement that needs to be printed about each celeb"""
    return f"\n{choice['name']}, a {choice['description']} from {choice['country']}"

def end_statements(first, second, guess):
    if first > second:
        return guess == "a"
    elif second > first:
        return guess == "b"
        


#Game Function
def higher_lower_game():
    """The actual game, makes it easier to count and run through if it's a function."""
    from game_data import data
    count = 0
    print(logo)
    stop_game = False

    while stop_game == False:

        #Defining/printing the first and second option while accounting for when they are the same and changing one
        if count == 0:
            first = definer()
            print(speech(first))
        else:
            first = second
            print(speech(first))
        print(vs)
        second = definer()        
        if second == first:
            while second == first:
                second = definer()
                print(speech(second))
        else:
            print(speech(second))

        #Player guess
        guess = input("\nWho do you think has the most instagram followers? A/B\n").lower()
        
        #Endgame
        first_follows = first["follower_count"]
        second_follows = second["follower_count"]
        move_on = end_statements(first_follows, second_follows, guess)
        clear()
        print(logo)
        if move_on == True:
            count += 1
            print(f"You're right! Your score is {count}")
        else:
            stop_game = True
            print(f"That's incorrect. Final score is {count}")

    #Restart input
    again = input("Would you like to play again? Y/N").lower()
    if again == "y":
        clear()
        higher_lower_game()

higher_lower_game()
