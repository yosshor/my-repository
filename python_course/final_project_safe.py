"""
@author: yosi shor
"""


def hangman(i):
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
    pictures_tree = {1 : picture_1, 2 : picture_2, 3 : picture_3,
                        4 : picture_4, 5 : picture_5, 6 : picture_6,
                        7 : picture_7}
  
    return (pictures_tree[i])
    
     



def welcome_screen():
    """this function just show us the welcome screen, and tell us how many tries
        we have to guess the secret word"""
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
    print("%s" , hangman_ascii_art)
    print(max_tries)
    


def check_win(secret_word, old_letters_guessed):
    """the func check if the old_letters_guessed its in secret_word.
       :param secret_word : secret_word value
       :param old_letters_guessed : old_letters_guessed value
       :type secret_word : list
       :type old_letters_guessed : list
       :return : the func will return the secret_word with letters you gueesed and True if you guess all the letters
       :rtype : list
       """ 
    if '_' in show_hidden_word(secret_word, old_letters_guessed):
        return False
    return True
        
    

    
def show_hidden_word(secret_word, old_letters_guessed):
    """the func check if the old_letters_guessed its in secret_word.
       :param secret_word : secret_word value
       :param old_letters_guessed : old_letters_guessed value
       :type secret_word : list
       :type old_letters_guessed : list
       :return : the func will return the secret_word with letters you gueesed and True if you guess all the letters
       :rtype : list
       """ 
    t = []
    r = []
    for i in range(len(old_letters_guessed)):
        if old_letters_guessed[i] in secret_word:
            t.append(format(old_letters_guessed[i]))
    for i in range(len(secret_word)):
        if secret_word[i] in t:
            r.append(secret_word[i] + '')
        else:
            r.append('_')
    return ' '.join(r)
 


def check_valid_input(letter_guessed, old_letters_guessed):
    """This func check the input that insert from the user, and if the letter is alpha and not number,
       and not sign like $, and also check if the len of this letter is one.
       :param letter_guessed : letter_guessed value
       :param old_letters_guessed : old_letter_guessed value
       :type letter_guessed : char 
       :type old_letters_guessed : list
       :return : if all the condition is True the func return True else False
       :rtype : bool True or False
    """
    new_letter = letter_guessed.lower()
    if new_letter.isalpha() == True :
        if len(new_letter) == 1 :
            if new_letter not in old_letters_guessed:
                return True
    return False
    
    

def try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word, wrong_word):
    """this func tell us if you insert already this letter or if its new in the list,and if its one letter in English
    :param letter_guessed : letter_guessed value
    :param old_letters_guessed : old_letters_guessed value
    :type letter_guessed : char / letter
    :type old_letters_guessed : list
    :return : the func will return if the new letter that is letter_guessed if its excist in the old_letters_guesses 
             or its new, if its new and it's one letter in English the func will return True, else False.
    :rtype : list
    """
    new_letter = letter_guessed.lower()
    new_wrong_letter = letter_guessed.lower()

    if check_valid_input(letter_guessed, old_letters_guessed) is True:
         if ((new_letter not in secret_word) and (check_valid_input(new_letter, old_letters_guessed) is True)) :
              wrong_word += new_wrong_letter
              print(hangman(len(wrong_word) + 1))
         old_letters_guessed += new_letter
         return True
      
    if ((new_letter in old_letters_guessed) or (new_letter.isalpha() == False) or (len(new_letter) > 1)):
        print('X')
        return show_tried_letters(old_letters_guessed)
    



def show_tried_letters(old_letters_guessed): 
    """this function show us the letters that in old_letters_guessed with sign.
       :param old_letters_guessed : old_letters_guessed value
       :type old_letters_guessed : list
       :return : the func return all the argument in the list with right sign.
       :rtype : list
       """
    t = []
    sord_old_letters = sorted(old_letters_guessed)
    for i in range(len(old_letters_guessed)):
        if i < len(sord_old_letters) - 1:
            t.append(format(sord_old_letters[i] + ' -> '))
        elif (i == len(sord_old_letters) - 1):    
            t.append(format(sord_old_letters[i]))       
    print(' '.join(t))



def convert(string): 
    li = list(string.split(" ")) 
    return li 


def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist


def choose_word(file_path, index):
    """this func get two parameters 1.is str that represent the file path
        2. ii the number call it index that reperesent the word position in
          file path, and sort the words in the file.
    :param file_path : file_path value
    :param index : index value
    :type file_path : str
    :type index : int
    :return : the func will return what is the word in file according num of index that you insert.
     :rtype : tuple
     """
     
    word = []
    index_word = ''
    with open(file_path) as file:
        for line in file:
            word += line.split()
    new = ' '.join(unique_list(word))
    list_sent = convert(new)
    for i in range(1,len(list_sent) + 1):
        index %= len(list_sent)
        if i == index:
            index_word = list_sent[i - 1]
    return  index_word

def main():
    
    welcome_screen()
    file_path  = str(input("Enter your file path : "))
    index = int(input('Enter index : '))
    print("\nLet's start!\n")
    secret_word = choose_word(file_path, index)
    print(hangman(1))
    old_letters_guessed = []
    print(show_hidden_word(secret_word, old_letters_guessed))
    wrong_word = []
    max_trais = 7
    for i in range(1, 13):
        if len(wrong_word) <= max_trais :
            enter_letter(secret_word, old_letters_guessed, wrong_word)
            if  (check_win(secret_word, old_letters_guessed) == True) :
                print('WIN')
                return  'WIN'
            if (((len(wrong_word)) + 1 == max_trais ) and (check_win(secret_word, old_letters_guessed) == False)):
                print('YOU LOSE')
                return 'YOU LOSE'



def enter_letter(secret_word, old_letters_guessed, wrong_word):
    letter_guessed = input("Guess a letter : ")
    if check_valid_input(letter_guessed, old_letters_guessed) is False:
        try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word, wrong_word)
        enter_letter(secret_word, old_letters_guessed, wrong_word)        
    else:  
        try_update_letter_guessed(letter_guessed, old_letters_guessed, secret_word, wrong_word)
        print(show_hidden_word(secret_word, old_letters_guessed))
        return letter_guessed

if __name__ == "__main__":
    main()
