
# Modifying Hangman to select randomly from a list of words.
import random

def hangman():
    wrong = 0
    stages = ["___________             ",
              "|                       ",
              "|            |          ",
              "|            0          ",
              "|           /|\         ",
              "|           / \         ",
              "|                       "
              ]
    word_list = ["dog", "cat", "pig", "rat", "cow"]
    word = random.choice(word_list)
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) -1:
        print("")
        msg = "Guess a letter: "
        guess = input(msg)
        if guess in rletters:
            cind = rletters.index(guess)
            board[cind] = guess
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("\nYou win!")
            print(" ".join(board))
            print("\n".join(stages[0: len(stages) -1]))
            win = True
            break
    if not win:
        print("You lose! It was: {}.".format(word))
