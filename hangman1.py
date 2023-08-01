import random

def hangman():
    l1 = ["one", "two", "three", "four", "five"]
    rnumb = random.randint(0,4)
    word = l1[rnumb]
    wrong = 0
    stages = [" ",
              " _________         ",
              " |        |        ",
              " |        |        ",
              " |        O        ",
              " |       /|\       ",
              " |       / \       ",
              " |                 ",
              "_|_____________    "]
    remaining_lettrs = list(word)
    board = ["__"] * len(word)
    win = False
    print("welcome to hangman!! ")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "guess the letter: "
        guess = input(msg)
        if guess in remaining_lettrs:
            character_index = remaining_lettrs.index(guess)
            board[character_index] = guess
            remaining_lettrs[character_index] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        print("\n".join(stages[0:wrong + 1]))
        if "__" not in board:
            print("you win!! Word was: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("you loose! Word was:{}.".format(word))
hangman()