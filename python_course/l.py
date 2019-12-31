"""
@author: yosi shor
"""

from termcolor import colored

def hangman(i):
    """ This function contains all Hangman's images in dictionary, and displays the correct image with colored
        for the number of the wrong guess.
        :return: right picture for the number of wrong guess
        :rtype: str
    """

    picture_1 = "    x-------x  "
    picture_2 = """
        x-------x
        |
        |
        |
        |
        |    
        """

    picture_3 = """
        x-------x
        |       |
        |       0
        |
        |
        |
    """
    picture_4 = """ 
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """
    picture_5 = """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        | 
    """
    picture_6 = """ 
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |  
    """
    picture_7 = """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
    """
    HANGMAN_PHOTOS = {1 : colored(picture_1, 'green'), 2 : colored(picture_2, 'blue'),
                      3 : colored(picture_3, 'red'), 4 :  colored(picture_4, 'cyan'),
                      5 : colored(picture_5, 'yellow'), 6 : colored(picture_6, 'white'),
                      7 : colored(picture_7, 'magenta')}
    return (HANGMAN_PHOTOS[i])



def welcome_screen():
    """This function show us the welcome screen for hangman,
       and tells the user for how many tries  he have to guess the secret word.
    """
    hangman_ascii_art = (""" 
      _    _                                         
     | |  | |                                         
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __   
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  
     | |  | | (_| | | | | (_| | | | | | | (_| | | | | 
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                          __/ |                       
                         |___/|           
                         """)

    max_tries = 6
    print(colored(hangman_ascii_art, 'green'))
    print(max_tries)



def check_win(secret_word, old_letters_guessed):
    """The function checks if all the letters in secret_wordare exist in old_letters_guessed.
       :param secret_word: secret_word value
       :param old_letters_guessed: old_letters_guessed value
       :type secret_word: str
       :type old_letters_guessed: list
       :return:  True if you guessed all the letters in secret_word else False
       :rtype: bool
    """
    if '_' in show_hidden_word(secret_word, old_letters_guessed):
        return False
    return True



def show_hidden_word(secret_word, old_letters_guessed):
    """The function checks if the letters in old_letters_guessed is in secret_word,
        and display the secret_word with the letters you guessed right and the other letters hidden.
       :param secret_word: secret_word value
       :param old_letters_guessed: old_letters_guessed value
       :type secret_word: list
       :type old_letters_guessed: list
       :return: the func will return the secret_word with letters you gueesed True, and the other letters with '_'
       :rtype: list
    """
    temp_letters = []
    secret_guessed_true = []
    for i in range(len(old_letters_guessed)):
        if old_letters_guessed[i] in secret_word:
            temp_letters.append(format(old_letters_guessed[i]))
    for i in range(len(secret_word)):
        if secret_word[i] in temp_letters:
            secret_guessed_true.append(secret_word[i] + '')
        else:
            secret_guessed_true.append('_')
    return ' '.join(secret_guessed_true)



def check_valid_input(letter_guessed, old_letters_guessed):
    """ The function checks if the new input letter is correct, that mean if the letter is alpha
        and not number or sign, and also check if the length of this letter is one.
       :param letter_guessed: letter_guessed value
       :param old_letters_guessed: old_letter_guessed value
       :type letter_guessed: str
       :type old_letters_guessed: list
       :return: True if all the conditions is True, else False
       :rtype: bool
    """
    new_letter = letter_guessed.lower()
    if new_letter.isalpha() == True:
        if len(new_letter) == 1:
            if new_letter not in old_letters_guessed:
                return True
    return False



def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word, wrong_letter):
    """This function checks if the new letter from the user are exist in secert_word, if not
        it add the letter in another variable and subtracting 1 from your num of try.
        :param letter_guessed: letter_guessed value
        :param old_letters_guessed: old_letters_guessed value
        :param secret_word: secret_word value
        :param wrong_letter: wrong_letter value
        :type letter_guessed: str
        :type old_letters_guessed: list
        :type secret_word: str
        :type wrong_letter: list
        :return: If the letter not in secret_word the function floting next picture in Hangman, and also will
                show the secret_word with the letter you guessed right
        :rtype: bool, func
    """
    new_letter = letter_guessed.lower()
    new_wrong_letter = letter_guessed.lower()

    if check_valid_input(letter_guessed, old_letters_guessed) is True:
         if (new_letter not in secret_word):
              wrong_letter += new_wrong_letter
              print(':( ')
              print(hangman(len(wrong_letter) + 1))
         old_letters_guessed += new_letter
         return True

    if ((new_letter in old_letters_guessed) or (new_letter.isalpha() == False) or (len(new_letter) > 1)):
        print('X')
        return show_tried_letters(old_letters_guessed)



def show_tried_letters(old_letters_guessed):
    """sorting the letters in old_letters_guessed, and show arrow between each letter
       :param old_letters_guessed: old_letters_guessed value
       :type old_letters_guessed: list
       :return: combining sorted letters with arrow together
       :rtype: str
    """
    letters_with_arrow = []
    sord_old_letters = sorted(old_letters_guessed)
    if len(old_letters_guessed) == 0:
        return

    for i in range(len(old_letters_guessed)):
        if i < len(sord_old_letters) - 1:
            letters_with_arrow.append(format(sord_old_letters[i] + ' -> '))
        elif (i == len(sord_old_letters) - 1):
            letters_with_arrow.append(format(sord_old_letters[i]))
    print(' '.join(letters_with_arrow))



def unique_list(words):
    """Takes the list and sorts it so there are no duplicate words
      :param words: words value
      :type words: list
      :return: sort list without multiplied word
      :rtype: list
   """
    ulist = []
    [ulist.append(x) for x in words if x not in ulist]
    return ulist


def choose_word(file_path, index):
    """ Get the file path, and the index, read and sorting the file
        :param file_path: file_path value
        :param index: index value
        :type file_path: str
        :type index: int
        :return: what is the word in the file, according the index position
        :rtype: str
     """
    word = []
    index_word = ''
    with open(file_path) as file:
        for line in file:
            word += line.split()
    new = ' '.join(unique_list(word))
    list_sent = list(new.split(" "))
    for i in range(1,len(list_sent) + 1):
        index %= len(list_sent)
        if i == index:
            index_word = list_sent[i - 1]
    return  index_word




def check_the_file_path():
    """User need to insert file path, and the function checks if the file path its legal,
        that mean if the file_path is exist.
       :return: the file path if legal, else the function raise an error and the user need to try again
       :rtype: str
    """
    file_path = []
    while True:
      try:
         file_path =  str(input("Enter your file path : "))
         open(file_path)
         return file_path
      except:
         print("Your file path is incorrect!")
         continue


def check_index():
    """Checks if the index is type int.
       :return: index if the index is int, else the function raise an error and ask the user for to try again
       :rtype: int
    """
    index = 0
    while True:
      try:
         index = int(input("Enter index: "))
         return index
      except ValueError:
         print("Your index is not an integer!")
         continue


def enter_letter(secret_word, old_letters_guessed, wrong_letter):
    """ The function ask from the user to guess a letter and checks if you have entered it before or the character
        is incorrect, If these conditions are met The function will ask for a new letter that it is not excist in the
        old_letters_guessed list, if the letter is legal and its not excist in the old_letters_guessed list and its
        in secret_word, the function will send it to another function to shown the secret_word with the letter you
        guessed right, and the rest of the letters are hidden.
        :param secret_word: secret_word value
        :param old_letters_guessed: old_letters_guessed value
        :param wrong_letter: wrong_letter value
        :type secret_word: str
        :type old_letters_guessed: list
        :type wrong_letter: list
        :return: the new legal letter
        :rtype: str
    """
    letter_guessed = input("Guess a letter: ")
    if check_valid_input(letter_guessed, old_letters_guessed) is False:
        try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word, wrong_letter)
        enter_letter(secret_word, old_letters_guessed, wrong_letter)
    else:
        try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word, wrong_letter)
        print(show_hidden_word(secret_word, old_letters_guessed))
        return letter_guessed


def main():
    """This function combinnig all other functions together and call the right function for to do the right things,
       at the beginig is shown us the welcome_screen after that the function ask from the user for to insert the
       file path and also index, the function send it to the right function for the right performance
       :return: LOSE if you traid all your tries guess and you fialed to guessed right, or WIN if you guessed
               right the all letters in the secret word
       :rtype: bool
    """
    welcome_screen()
    file_path = check_the_file_path()
    index = check_index()
    print("\nLet's start!\n")
    secret_word = choose_word(file_path, index)
    print(hangman(1))
    old_letters_guessed = []
    print(show_hidden_word(secret_word, old_letters_guessed))
    wrong_letter = []
    MAX_TRIES = 7
    while len(wrong_letter) <= MAX_TRIES :
        enter_letter(secret_word, old_letters_guessed, wrong_letter)
        if  (check_win(secret_word, old_letters_guessed) == True) :
            print('YOU WIN')
            return  True
        if (((len(wrong_letter)) + 1 == MAX_TRIES ) and (check_win(secret_word, old_letters_guessed) == False)):
            print('YOU LOSE')
            return False





if __name__ == "__main__":
    main()
