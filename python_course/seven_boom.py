def seven_boom(end_number):
    """This function print list that include all the number until end number, and if its including seven or num % 7 == 0 
        the func retutn BOOM 
        :param end_number : end_number value
        :type end_number : number
        :return : the func will return BOOM if all the conditions is True
        :rype : list 
    """
    result = []
    for i in range(end_number):
        if i % 7 == 0:
            result.append('BOOM')
            continue
        if i % 10 == 7:
            result.append("BOOM")
            continue
        result.append(i)
    return result
print(seven_boom(18))