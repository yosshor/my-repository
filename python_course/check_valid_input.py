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
                old_letters_guessed += new_letter
                return True
                
            
    return False
    
    