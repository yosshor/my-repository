
def last_early(my_str):
    seperate_word = my_str.split()

    if seperate_word[0][-1] == seperate_word[1][-1]: 
         return True
    if my_str[0] == my_str[-1]:
         return True
    if len(seperate_word[0]) == 1:
         return False
    return False

last_early('happy birthday')