def are_lists_equal(list1, list2):
    """This function will check if list1 is equal to the list2
       :param list1 : list1 value
       :param list2 : list2 value
       :type list1 : list
       :type list2 : list
       :return : the function will return True if the two list is equal, else return Flase.
       :rtype : list 
    """
    """ #if (list1.sort() == list2.sort()):
    we have onther solution, we can write 
    list1.sort()
    list2.sort()
    if list1 == list2 :
        return True 
    return False
    """
    if sorted(list1) == sorted(list2):
          return True
    else:
        return False



list1 = [0.6, 1, 2, 3] 
#list2 = [3, 2, 0.6, 1] 
list2 = [9, 0, 5, 10.5] 
are_lists_equal(list1, list2) 

list1 = [0.6, 1, 2, 3] 
list2 = [3, 2, 0.6, 1] 
#list2 = [9, 0, 5, 10.5] 
are_lists_equal(list1, list2) 