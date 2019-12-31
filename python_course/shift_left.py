def shift_left(my_list):
    """ this function get a list that has three argument and the func move each argument to the left.
        :param my_list : my_list value
        :param new_list : new_list value
        :type my_list : list
        :type new_list : list
        :return : the function will return the list shifted one left
        :rtype : list 
    """
    #my_list = []
    new_list = my_list[1:]
    new_list.insert(2,my_list[0])
    return new_list

def main():
    shift_left([0,1,2])

if __name__ == "__main__":
    main()

  
   

