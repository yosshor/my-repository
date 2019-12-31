def substracting(first_num, second_num):
    """This function take two argument and substracting the second_num from the first_num
        :param first_num : first_num value
        :param second_num : second_num value
        :type first_num : int or every num that you want to insert
        :type second_num : int or every num that you want to insert
        :return : This function will return the result of substracting the second_num from the first_num
        :rtype : the result can be any type of result, its depend what you insert in the beginning"""
    print (first_num - second_num)

def main():
    substracting(12894, 11672)

if __name__ == "__main__" :
    main()

""" this is for if you want to check this func and import that you need to write this
    import substracting
    substracting.substracting(123, 100)
    and if you want to see the document about this function you neet to write help(function) example here 
    you need to write help(substracting) or substracting.__doc__ its another way to see the docustring"""