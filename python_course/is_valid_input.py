def  is_valid_input(letter_guessed):
    """this function will check the input (that is letter_guessed) if is a one letter or something alse,
       if its one English letter the function will return True, other way the function return False.
       :param letter_guessed : letter_guessed value.
       :type letter_guessed : letter or char.
       :return : The function will return True if the letter_guessed is one English leeter, alse False.
       :rtype : boolian """

    if letter_guessed.isalpha() == True :
        if len(letter_guessed) == 1 :
            return True
    return False
    