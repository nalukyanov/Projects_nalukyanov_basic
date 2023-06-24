import random

print("Hello, user!")
print("_" * len("Hello, user!"), "\n")

HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# слова для игры
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


def main():
    guesser()


def show_guess(w):
    first_message = ["Your word is: ", "_" * len(w), ". Guess!", "\n"]
    return first_message


def word():
    w = random.choice(words)
    return w


def guesser():
    w = word()
    for i in show_guess(w):
        print(i, end="")
    word_to_guess = [i for i in w]
    testing_word = [i for i in word_to_guess]
    word_in_progress = ["_" for _ in range(len(word_to_guess))]
    mistakes = 0
    while mistakes < 7:
        letter = input("Guess letter: ")
        if not letter.isalpha():
            print("Please, type only letters")
            continue
        elif len(letter) != 1:
            print("Please, enter one letter at a time")
            continue
        elif letter in word_to_guess:
            place = word_to_guess.index(letter)
            word_to_guess[place] = "*"
            word_in_progress[place] = letter
            if word_in_progress == testing_word:
                print(f"You won, pal! The word was a {w}")
                break
        elif letter not in word_to_guess:
            mistakes = mistakes + 1
            print("Whoops! Wrong letter")
            print(HANGMAN_PICS[mistakes-1])

        for i in word_in_progress:
            print(i.capitalize(), end="")
        print("\n")
    else:
        print(f"Sorry, you lost! Your word was {w}")


if __name__ == '__main__':
    main()
