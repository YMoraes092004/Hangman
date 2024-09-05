import random
import Hangman_def

with open('WORDS.txt', 'r') as file:
    # Read all lines into a list
    lines = file.readlines()

# Choose a random line
cor_word = random.choice(lines).strip().lower()
inc_att = 0
cor_att = 0
rev_word = ["_" for _ in cor_word]

print("""Welcome to Hangman:
      you have 6 wrong attempts to guess the word before you have hung the man. 
      Every guess you make must be a single letter. GOOD LUCK!""")

while(inc_att < 6 and "_" in rev_word):
    guess = input("Guess a letter: ").lower()
    
    while guess.isnumeric() or len(guess) != 1:
        guess = input("You have entered an incorrect guess, try again: ").lower()


    if guess in cor_word:
        for i in range(len(cor_word)):
            if cor_word[i] == guess:
                rev_word[i] = guess
        cor_att = Hangman_def.upd_cor_att(cor_att)
    else:
            inc_att = Hangman_def.upd_inc_att(inc_att)

    Hangman_def.dis_cor_guesses(rev_word)
    Hangman_def.display_hangman(inc_att)

if "_" not in rev_word:
    print("You have won, congrats!! The correct word was", cor_word)
else:
    print("You have lost, too bad!! The correct word was", cor_word)



       





