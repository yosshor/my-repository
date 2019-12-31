from show_tried_letters import show_tried_letters

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
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
    if new_letter.isalpha() == True :
        if len(new_letter) == 1 :
            if new_letter not in old_letters_guessed:
                old_letters_guessed += new_letter
                print(list(old_letters_guessed))
                return True          
    print('X')
    show_tried_letters(old_letters_guessed)
    print('False') #return False  

def main():
    old_letters_guessed = ['a', 'p', 'c', 'f']  
    try_update_letter_guessed('s', old_letters_guessed) 
    try_update_letter_guessed('f', old_letters_guessed) 

if __name__ == "__main__":
    main()