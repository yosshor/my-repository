def format_list(my_list):
    """This function take the structure and print only the add location plus "and" with the last of the list.
        :param my_list : list
        :return : the function will return only the even location plus the last in the list.
        :rtype: list
        """
    return ", ".join(my_list[0::2]) + ", and " + my_list[-1]

def main():
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"] 
    format_list(my_list)

if __name__ == "__main__":
    main()