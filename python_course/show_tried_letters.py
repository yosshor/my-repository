def show_tried_letters(old_letters_guessed):
    """this function show us the letters that in old_letters_guessed with sign.
       :param old_letters_guessed : old_letters_guessed value
       :type old_letters_guessed : list
       :return : the func return all the argument in the list with right sign.
       :rtype : list
       """
    t = []
    for i in range(len(old_letters_guessed)):
        t.append(format(old_letters_guessed[i]) + '-->')
    print(' '.join(t))


def main():
    old_letters_guessed = ['a', 'p', 'c', 'f'] 
    show_tried_letters(old_letters_guessed) 

if __name__ == "__main__":
    main()