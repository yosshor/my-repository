def extend_list(list_x, list_y):
    """ This function take the list_y and put it in the first new stracture and than append list_x to the same new list
        :param list_x : list_x value
        :param list_y : list_y value
        :param new : new value
        :type list_x : list
        :type list_y : list
        :type new : list
        :return : the function will return a new list that contain list_y at first and after that list_x
        :rtype : list """
    new = []
    for i in range(len(list_y)):
            new.append(list_y[i])
    for j in range(len(list_x)):
            new.append(list_x[j])
    return new

def main():
    extend_list([4,5,6],[1,2,3])

if __name__ == "__main__":
    main()