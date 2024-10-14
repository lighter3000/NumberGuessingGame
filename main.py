import random


def start():
    print(
        """
Welcome to the Number Guessing Game!\n
I'm thinking of a number between 1 and 100.\n
You have 5 chances to guess the correct number.\n
""")

    playing = True
    while playing:

        print("""
\n
Please select the difficulty level:\n
1. Easy (10 Chances)\n
2. Medium (5 Chances)\n
3. Hard (3 Chances)\n
\n
        """)

        chances = get_difficulty()


        print("Let's start the game")

        game(chances)

        while True:
            answer = input("Want to play again? (Y/N): ")

            if answer == "Y" or answer == "y":
                break
            elif answer == "N" or answer == "n":
                print("Thank you for playing!")
                return
def game(chances):
    random_number = random.randint(1, 100)
    guesses = 0
    while chances > 0:
        guesses = guesses + 1
        guessed_number = int(input("Enter your guess: "))
        if type(guessed_number) != int:
            print("Sorry, your input is not an integer")
        if guessed_number == random_number:
            print("Correct!")
            print(f"Congratulations! You guessed the correct number in {guesses} attempts.")
            break
        elif guessed_number < random_number:
            print(f"Incorrect! The number is higher than {guessed_number}.")
        elif guessed_number > random_number:
            print(f"Incorrect! The number is lower than {guessed_number}.")

        chances = chances - 1

    if chances == 0:
        print(f"Sorry, you have not guessed the correct number. The correct number was {random_number}")

def get_difficulty():
    while True:
        difficulty = input("Enter your choice: ")
        if difficulty == "1":
            print("Great! You have selected the Easy difficulty level.")
            return 10
        elif difficulty == "2":
            print("Great! You have selected the Medium difficulty level.")
            return 5
        elif difficulty == "3":
            print("Great! You have selected the Hard difficulty level.")
            return 3
        else:
            print("Sorry, you have not selected a given difficulty level.")

if __name__ == "__main__":
    start()