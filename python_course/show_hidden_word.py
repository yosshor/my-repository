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
    print(' '.join(r))
    if '_' in r:
        return False
    return True


def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'w', 'j', 'm', 'y', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))

if __name__ == "__main__":
    main()