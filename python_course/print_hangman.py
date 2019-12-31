def print_hangman(num_of_tries):
    """this func show the suitable picture for right num_of_tries
       :param num_of_tries : num_of_tries
       :type num_of_tries : int
       :return : the func print the right num picture for what you insert
       :rtype : str
       """ 
    
    picture_0 = "    x-------x  "
    picture_1 = """
        x-------x
        |
        |
        |
        |
        |    
        """
    picture_2 = """
        x-------x
        |       |
        |       0
        |
        |
        |
    """
    picture_3 = """ 
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """
    picture_4 = """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        | 
    """
    picture_5 = """ 
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |  
    """
    picture_6 = """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
    """
    hangman_photos = {0 : picture_0, 1 : picture_1, 
    2 : picture_2, 3 : picture_3, 4 : picture_4,
    5 : picture_5, 6 : picture_6}
    
    print(hangman_photos[num_of_tries])
    
   
    
print_hangman(6)


