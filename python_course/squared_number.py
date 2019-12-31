def squared_numbers(start, stop):
    """This func will get two num and take start power 2, and statr + 1 until start equal to stop and than 
       the func stop running.
       :param start : start value 
       :param stop : stop value
       :type start : number
       :type stop : number
       :return : the func return start power two until start equal to stop
       :rtype : number
       """
    t = 0
    while start < stop :
        t = start ** 2
        start += 1
        print(t)
    
squared_numbers(4, 8)  