# This program implements a hangman game in Python
# The user must guess one of 160 different possible words which are stored in a text file
# The text file contains a list of different items from the MOBA game Dota 2.

# Import statements
import hangman_printer
import random


# Function that returns a random word from the text file
def get_chosen_word():
    file = open("word_list.txt", "r")
    word_list = file.read().splitlines()
    file.close()
    return word_list[random.randint(0, len(word_list) - 1)]


# Function that takes a word and returns the corresponding "display string"
# The display string is a list of characters with all non-space characters replaced with an underscore
def create_display_string(word):
    string = []
    for letter in word:
        if letter != " ":
            string.append("_")
        else:
            string.append(" ")
    return string


# Function that prints the display string with a space inserted between each character in the string
def print_string(string):
    for item in string:
        print(item + " ", end='')
    print("\n")


# Function that returns the appropriate game status based on how many guesses are remaining and
# whether there are any letters that have yet to be guessed
def get_game_status(guesses, string):
    if guesses == 6:
        return 1
    for item in string:
        if item == "_":
            return 0
    return 2


# Function that outputs the appropriate data when the game is over depending on whether the user won or lost
def end_game(status, guesses, string, word):
    if status == 1:
        hangman_printer.print_hangman(guesses)
        print_string(string)
        print("You Lose! The word was " + word + ".")
    elif status == 2:
        print()
        print_string(string)
        print("You Win! The word was " + word + ".")


# Chooses a word from the text file, creates the corresponding display string and sets up game variables
chosen_word = get_chosen_word()
display_string = create_display_string(chosen_word)
incorrect_guesses = 0
incorrect_guesses_list = []
game_status = 0

# Continuously loops as long as the user has not won/lost the game yet
while game_status == 0:
    # Print the appropriate data and ask for the user's guess
    hangman_printer.print_hangman(incorrect_guesses)
    print_string(display_string)
    print("Letters Not In Word: ", end='')
    print_string(incorrect_guesses_list)
    user_guess = input("Your Guess: ").lower()

    # The guess is only considered if it is valid (i.e. if it is 1 character in length)
    if len(user_guess) == 1:
        # Assume that the letter guessed by the user is not present in the word
        is_char_present = False
        # If the letter is present in the chosen word, the corresponding characters in the display string are changed
        # from underscores to the correctly identified letter
        for index in range(0, len(chosen_word)):
            if chosen_word[index].lower() == user_guess:
                display_string[index] = chosen_word[index].lower()
                is_char_present = True
        # If the letter is not present in the chosen word and it has not already been guessed, it is added to the list
        # of incorrect guesses and the incorrect guess counter is incremented
        if not is_char_present and incorrect_guesses_list.count(user_guess) == 0:
            incorrect_guesses += 1
            incorrect_guesses_list.append(user_guess)
        # Check to see if the game is won, lost, or should continue
        game_status = get_game_status(incorrect_guesses, display_string)

# Display the appropriate information when the game is over
end_game(game_status, incorrect_guesses, display_string, chosen_word)
