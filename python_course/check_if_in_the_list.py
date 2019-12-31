def check_the_list(my_list):
    """


       """
    worng_item = []
    n = int(input('enter num between 1 - 9 :'))
    if n == 1:
        print(my_list)
        check_the_list(my_list)
        
    if n == 2:
        print('you have {} item in this list'.format(len(my_list)))
        check_the_list(my_list)

    if n == 3:
        check_item = input('enter item to chenk if it in the list :')
        if check_item in my_list:
            print('Yes its on the list')
            print('its in the list {} times'.format(my_list.count(check_item)))
        else:
            print('its not on the list')
        check_the_list(my_list)

    if n == 4:
        check_item = input('enter item to chenk how many times its in the list :')
        if check_item in my_list:
            print('its in the list {} times'.format(my_list.count(check_item)))
        else:
            print('its not on the list')
        check_the_list(my_list)
    
    if n == 5:
        want_remove = input('what do you want to remove from the list? choose one word :')
        if want_remove in my_list:
            my_list.remove(want_remove)
            print('your new list is : {}'.format(my_list))
        check_the_list(my_list)

    if n == 6:
        new_item = input('enter your new item : ')
        if new_item == '':
            new_item = 0
        else:
            my_list.append(new_item)
        print(my_list)
        check_the_list(my_list)

    if n == 7:
        for i in range(len(my_list)):
            if ((my_list[i].isalpha() == False) or (len(my_list[i]) < 3)):
                worng_item += my_list[i] + ' '
            print('its illegal word from your list : {}'.format(worng_item))
            check_the_list(my_list)

    if n == 8:
        for i in range(len(my_list) - 2):
            if (my_list.count(my_list[i]) != 1):
                worng_item += my_list[i] + ' '
                new_list = my_list.remove(my_list[i])
        print('we remove the wrong item from your list : {}'.format(''.join(worng_item)))
        print('its your new list : ', my_list)
        check_the_list(my_list)

    if n == 9:
        pass

check_the_list(['Milk', 'Cottage', 'Tomatoes', 'll', '32123', 'yoss', 'yoss', 'nash', 'nash'])