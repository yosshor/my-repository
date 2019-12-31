def is_greater(my_list, n):
    """This func checking if have biger number than n.
       :param my_list : my_list value
       :param n : n value
       :type my_list : list
       :type n : number
       :return : The func return all the greater number in my_list that greater than n
       :rtype : list
       """
    new = []
    for i in range(len(my_list)):
        if my_list[i] > n:
            new.append(my_list[i])
    return new

is_greater([1, 30, 25, 60, 27, 28], 28)