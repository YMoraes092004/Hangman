def check_letter(x):
    x = x.lower()
    return x

def update_wrong_guesses(x):
    x =+ 1
    return x

def display_hangman(x):
    if(x == 1):
        print("""
                 _____
                 |   |
                 |   O
                 |
                 |
              ___|____""")
        
    if(x == 2):
        print("""
                 _____
                 |   |
                 |   O
                 |   | 
                 |
              ___|____""")
        
    if(x == 3):
        print("""
                 _____
                 |   |
                 |  _O
                 |   |
                 |
              ___|____""")
        
    if(x == 4):
        print("""
                 _____
                 |   |
                 |  _O_
                 |   |
                 |
              ___|____""")
    
    if(x == 5):
        print("""
                 _____
                 |   |
                 |  _O_
                 |   |
                 |   L
              ___|____""")
        
    if(x == 6):
        print("""
                 _____
                 |   |
                 |  _O_
                 |   |
                 |   LL
              ___|____""")

#where x is the guess and cor_word is the correct string        
def dis_cor_guesses(revealed_word):
    print(" ".join(revealed_word))

def upd_cor_att(x):
    return x + 1

def upd_inc_att(x):
    return x + 1


    


