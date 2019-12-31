def arrow(my_char, max_length):
    """


    """
    for i in range(0,max_length + 1):
        new = my_char * i
        print(new)
    for j in range(max_length+1,0,-1):
        new = my_char * j
        print(new)



#         print(new)

print(arrow('$', 5))
