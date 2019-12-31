def numbers_letters_count(my_str):
    """ This function run all over the list that i call it my_str and count how many letters and numbers have there
        :param my_str : my_str value
        :type my_str : list
        :return : the func return number that will show us how many letters or numbers have in my_str
        :rtype : list 
        """
    is_digit = 0
    for i in range(len(my_str)):
        if my_str[i].isdigit() == True:
            is_digit += 1
    the_sum_letters = len(my_str) - is_digit
    result = [is_digit, the_sum_letters]
    return result

def main():
    print(numbers_letters_count("Python 3.6.3"))

if __name__ == "__main__":
    main()