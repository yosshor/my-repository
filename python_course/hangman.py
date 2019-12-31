import random

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
print("%s /n/n%d" , hangman_ascii_art ,  max_tries)
print(max_tries)
input_string = input("please enter a word :")
len_str_input = len(input_string)
print("_ " *len_str_input)

#second exercise
guess_letter = input("guess a letter :")

#if guess_letter.isdigit() == True:

# i wrote a new function for checking if the letter_guess is True or False you need to check in the library.
"""def  is_valid_input(letter_guessed):
   this function will check the input (that is letter_guessed) if is a one letter or something alse,
       if its one English letter the function will return True, other way the function return False.
       :param letter_guessed : letter_guessed value.
       :type letter_guessed : letter or char.
       :return : The function will return True if the letter_guessed is one English leeter, alse False.
       :rtype : boolian 

    if letter_guessed.isalpha() == True :
        if len(letter_guessed) == 1 :
            return True
    return False
    """
change_latter = ''
if guess_letter.isalpha() == True :
    if len(guess_letter) > 1 :
        print('E1')
elif guess_letter.isalpha() == False :
    if len(guess_letter) == 1:
        print('E2')
else :
    print('E3') 

if guess_letter.isupper() :
    change_latter = guess_letter.lower()
    print(change_latter)
if guess_letter.islower() :
    print(guess_letter)

# if ((int(ord(guess_letter >= 65)) and (int(ord(guess_letter <= 90))))):
 #   print(guess_letter)

#elif (guess_letter == A - Z):
#    print(guess_letter.lower())


#lower_input = input_letter.lower()
#print(lower_input)

#print(" {}  {} ".format(hangman_ascii_art, max_tries))
#tries_to_fail = random.randint(5,10)
#print(tries_to_fail)

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
picture_of_three = [picture_1,picture_2, picture_3, picture_4, picture_5, picture_6, picture_7]
for picture in pictures_tree:
   print(pictures_tree[picture])

