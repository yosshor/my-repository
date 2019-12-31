def sort_prices(my_list):
    """
    """
    def takeSecond(elem):
        """
        """
        return elem[1]
    my_list.sort(key=takeSecond, reverse = True)
    print('Sorted list:', my_list)
products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
sort_prices(products)