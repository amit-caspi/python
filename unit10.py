def main():
    global HANGMAN_PHOTOS
    MAX_TRIES = 6 # a constant that represents the maximum number of failed attempts allowed.
    HANGMAN_PHOTOS = {1:"x-------x ", 2:
"""x-------x
 |
 |
 |
 |
 | """, 3:
"""x-------x
 |       |
 |       0
 |
 |
 | """, 4:
"""x-------x
 |       |
 |       0
 |       |
 |
 | """, 5:
"""x-------x
 |       |
 |       0
 |      /|\\
 |
 | """, 6:
"""x-------x
 |       |
 |       0
 |      /|\\
 |      /
 | """, 7:
"""x-------x
 |       |
 |       0
 |      /|\\
 |      / \\
 | """}
    opening_screen(MAX_TRIES)  
    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    while index <= 0:
        print ("The index is not valid!")
        index = int(input("Enter index: "))
    print ("\nLet's start!\n") 
    num_of_tries = 0 # The number of failed attempts by the player so far.
    print_hangman(num_of_tries) # opening 
    secret_word = choose_word(file_path, index)
    old_letters_guessed = []
    print(" ",show_hidden_word(secret_word, old_letters_guessed))
    print ("\n")
    while(not check_win(secret_word, old_letters_guessed)) and (num_of_tries < MAX_TRIES):
	# Check- if the game should continue (the user has not won yet \ still can make a mistake).
        letter_guessed = input("Guess a letter: ").lower()
        while not try_update_letter_guessed(letter_guessed, old_letters_guessed):
		# Check if the character guessed by the player is valid, 
		# and if not- Input up to a valid character.
            letter_guessed = input("Guess a letter: ").lower() 
        if letter_guessed not in secret_word:
            num_of_tries += 1
            print (":(")
            print_hangman(num_of_tries)
        print(show_hidden_word(secret_word, old_letters_guessed))
    if check_win(secret_word, old_letters_guessed):
        print ("WIN")
    else:
        print ("LOSE") 	
	
def opening_screen(MAX_TRIES):
    """
    The function prints the welcome screen- Hangman,
    and the maximum number of failed attempts.
    :param MAX_TRIES: a constant that represents the maximum number
	of failed attempts allowed in the game.
    :type MAX_TRIES: int
    :return: None
    """
    HANGMAN_ASCII_ART = """
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/ """ 
    #a constant that points to the string- that the function prints as part of the opening.
    print (HANGMAN_ASCII_ART)
    print (MAX_TRIES)
	
def print_hangman(num_of_tries):
    """
    The function prints photos of the hang man (the position) from the dictionary 
	HANGMAN_PHOTOS, depending on the key it receives (the key is num_of_tries + 1).
    :param num_of_tries: The number of failed attempts by the player so far. 
    :type num_of_tries: int
    :return: None
    """
    print ("\n", HANGMAN_PHOTOS[num_of_tries+1], "\n")

def choose_word(file_path, index): 
    """
    The function finds a word from a text file that will be used as the secret word
    for guessing (depending on the index it receives).
    :param file_path: a string that represents a path to a text file
    that contains space-separated words.
	:param index: an integer that represents the location of a particular
	word in the file.
    :type file_path: string
	:type index: int
    :return: the word in the index location, which will be used as
	the secret word for guessing.
    :rtype: string
    """
    with open (file_path, "r") as my_file:
       the_words = my_file.read() 
    words_splitted = the_words.split(" ")	   
    full_length_words= len(words_splitted) 
    word_index = int(index) % full_length_words - 1
    the_secret_word = words_splitted[word_index].lower()
    return(the_secret_word)
	
def show_hidden_word(secret_word, old_letters_guessed):
    """
    The function returns string which represents the secret word
    without the unguessed letters.
    :param secret_word: the secret word for guessing.
	:param old_letters_guessed: a list of letters that the player had previously guessed.
    :type secret_word: string
	:type old_letters_guessed: list (of strings)
    :return: a string which include letters (which the player guessed and in the
    secret word) and underlines (which the player has not guessed yet).
    :rtype: string
    """
    progress = ""  
    for letter in secret_word:
        if letter in old_letters_guessed:
            progress += letter + " " 
        else:
            progress += "_ "
    return progress

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    The function tries to update old letters guessed by input 
	(it checks if the input is valid and returnes an answer accordingly).
    :param letter_guessed: character that the player has guessed.
	:param old_letters_guessed: a list of letters that the player had previously guessed.
    :type letter_guessed: string 
	:type old_letters_guessed: list (of strings)
    :return: True / False, depending on- if the input received by the player is valid.
    :rtype: bool
    """
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print ("X")
        old_letters_guessed.sort()
        letters_guessed = ' -> '.join(old_letters_guessed)
        print (letters_guessed)
        return False
    else:
        old_letters_guessed.append(letter_guessed.lower())
        return True 

def check_valid_input(letter_guessed, old_letters_guessed):
    """
    The function checks validation of an input (char).
    :param letter_guessed: character that the player has guessed.
	:param old_letters_guessed: a list of letters that the player had previously guessed.
    :type letter_guessed: string 
	:type old_letters_guessed: list (of strings)
    :return: True / False, depending on- if the input (char) is valid.
    :rtype: bool
    """
    if ((len(letter_guessed) > 1) or (letter_guessed.isalpha() == False)
    or (letter_guessed.lower() in old_letters_guessed)):
        return False
    else: 
        return True
		
def check_win(secret_word, old_letters_guessed):
    """
    The function checks if the player has won.
    :param secret_word: the secret word for guessing.
	:param old_letters_guessed: a list of letters that the player had previously guessed.
    :type secret_word: string
	:type old_letters_guessed: list (of strings)
    :return: True / False, depending on- if all the letters that in the secret word are
	included in the list of letters that guessed (is player won).
    :rtype: bool
    """
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False 
    return True
	
if __name__ == '__main__':
    main()
	