# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:19:07 2019

@author: EGLOBAL
"""


def main():
    
    welcome_screen()
    file_path  = str(input("enter your file path : "))
    index = int(input('enter index : '))
    print("Let's start!")

    secret_word = choose_word(file_path, index)
    old_letters_guessed = []
    num_of_tries = len(old_letters_guessed)
    max_trais = 7
#    enter_letter(secret_word, old_letters_guessed, max_trais)

    for i in range(1, max_trais + 1):
        print(len(old_letters_guessed))
        if i <= max_trais:
            
            enter_letter(secret_word, old_letters_guessed, max_trais)
#            hangman(secret_word, num_of_tries)
            
        if  (check_win(secret_word, old_letters_guessed) == True) :
            return  'WIN'
        elif (len(old_letters_guessed) == max_trais ) and (check_win(secret_word, old_letters_guessed) == False):
            print('LOSE')
            return None

main()     


def enter_letter(secret_word, old_letters_guessed, max_trais):
    num_of_tries = len(old_letters_guessed)

    letter_guessed = input("Guess a letter : ")
    
    if check_valid_input(letter_guessed, old_letters_guessed) is False:
        try_update_letter_guessed(letter_guessed, old_letters_guessed)
        enter_letter(secret_word, old_letters_guessed, max_trais)
           
    
    elif (letter_guessed in secret_word) and (letter_guessed not in old_letters_guessed) :
        try_update_letter_guessed(letter_guessed, old_letters_guessed)
        print(show_hidden_word(secret_word, old_letters_guessed))
    else :
        
        hangman(secret_word, num_of_tries)  
        try_update_letter_guessed(letter_guessed, old_letters_guessed)
        print(show_hidden_word(secret_word, old_letters_guessed))
        return show_hidden_word(secret_word, old_letters_guessed)
    
    
    

#def do_some(secret_word, old_letters_guessed, letter_guessed, wrong_word):
#    lengh = len(wrong_word)
#    if (letter_guessed not in old_letters_guessed) and (letter_guessed not in secret_word) :
#        t += 1 
#        print(hangman(t))
#        print(t)
#    return t
#    
#    t = num_failed
#    if (letter_guessed not in old_letters_guessed) and (letter_guessed not in secret_word):
#        t += 1 
#        print(hangman(t))
#    return t
    
    
#do_some(secret_word, old_letters_guessed, letter_guessed)    
    


#try_update_letter_guessed
#

#         if check_valid_input(letter_guessed, old_letters_guessed) is True :    
            
    
#    old_letters_guessed = input_new_letter
#    
#    show_hidden_word(secret_word, old_letters_guessed)
#    
#
#        print(show_hidden_word(secret_word, old_letters_guessed))
#            
#    
#    print(hangman(secret_word))
#    
#    for i in 
#    
#
#    #is the sum of fails trais
#    hangman_photo = {} # i need to put all the pictures of hangman with num for each try
#    
#        
    

    
#    for picture in pictures_tree:
#        print(pictures_tree[picture])
    #        if (num_of_tries == max_trais) or (check_win(secret_word, old_letters_guessed) == True) :
#            check_win(secret_word, old_letters_guessed)
                    
    
#def main():
#    old_letters_guessed = ['a', 'p', 'c', 'f'] 
#    show_tried_letters(old_letters_guessed) 


#
#def main():
#    old_letters_guessed = ['a', 'p', 'c', 'f']  
#    try_update_letter_guessed('s', old_letters_guessed) 
#    try_update_letter_guessed('r', old_letters_guessed) 
#

          
        
#def g(letter_guessed, secret_word, old_letters_guessed):
#    lengh = []
#    if ((letter_guessed not in secret_word) and (check_valid_input(letter_guessed, old_letters_guessed) is True)) :
#        lengh += letter_guessed
#        print('hello')
#        print(hangman(len(lengh) + 1))


#    print('X')
#    print(list(old_letters_guessed))
#    return ('X \n {}'.format(list(old_letters_guessed)))  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    