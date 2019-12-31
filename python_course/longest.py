def longest(my_list) :
    """ This function get list and search the bigest word 
        :param my_list : my_list value
        :type my_list : list
        :return : the function return what is the longest word that you have in the list.
        :rtype : list
    """
    return max(my_list, key = len)
   


list1 = ["111", "234", "2000", "goru", "birthday", "09"]
longest(list1)