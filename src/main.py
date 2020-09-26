import random

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def guessed_so_far(secret_word, guesses):
    shown = secret_word

    # For every character that the player guessed
    # guesses = ['k', 'm', 'l']
    # k a a n
    # k _ _ _
    for character in ALPHABET:
        if character not in guesses:
            shown = shown.replace(character, '_')

    shown = ' '.join(shown)
    return shown


def generate_secret_word():
    WORD_POOL = ["computer", "extraordinary", "division", "spectacular", "lantern",
                 "psychologically", "extreme", "potato", "perseverance",
                 "execution", "diamond", "ambivert", "omnipresent", "ludicrous",
                 "angular", "beginner", "classical", "artwork", "museum",
                 "platypus", "anteater", "glucose", "electricity", "hospital", "intervention",
                 "intertwined", "endeavour", "ultimatum", "statement", "arrangement"]

    generated_secret_word = random.choice(WORD_POOL)
    return generated_secret_word


def is_valid_input(given_input, guesses_so_far):
    is_valid = True

    if given_input not in ALPHABET:
        is_valid = False
        print("Your guess should be in alphabet.")

    if len(given_input) > 1:
        is_valid = False
        print("You should guess a single character.")

    if given_input in guesses_so_far:
        is_valid = False
        print("You already guessed that character.")

    return is_valid


def get_input(guesses_so_far):
    guess = input("Make a guess: ").lower()

    while not is_valid_input(guess, guesses_so_far):
        guess = input("Make a guess: ").lower()

    return guess


def hangman(turns):
    # Initialize the game
    # Plays the hangman game and returns the result
    guesses = []
    did_player_win = False
    secret_word = generate_secret_word()    # Determine the secret word

    while turns > 0:
        # Get guess from player
        guess = get_input(guesses)
        guesses.append(guess)

        # Print the secret word
        word_shown = guessed_so_far(secret_word, guesses)
        print(word_shown)
        print("\n")

        # Check if player won the game already
        if "_" not in word_shown:
            did_player_win = True
            break

        # End of turn
        if guess not in secret_word:
            turns = turns - 1
            print("Turns left: ", turns)

    return did_player_win


if __name__ == "__main__":
    NUMBER_OF_TURNS = 10
    player_won = hangman(NUMBER_OF_TURNS)

    if player_won is True:
        print("Congratulations! You won! :)")
    else:
        print("You tried.. Next time.")
