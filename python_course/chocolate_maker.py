def chocolate_maker(small, big, x):
    """ This function take the argument small and big into a line 'x', if big + small will be equale to 'x' 
        the function will return True else the func return False, and we dont use with loop.
        num input : samll and big and x is int
        return :boolian True or False """
    big_new = big * 5
    
    if (small + big_new == x) or (big_new == x) or (small == x):
        return True
    return False
 

