
ages = [13, 14, 17, 18 , 19]
sum_age = 0


def filter_age(a = 13, b = 13, c = 13):
    """ This func will return the sum of ages if they all the number without [13, 14, 17,18, 19] if the a or b or c
         are in the list the func compute them like zero and return the sum of them/
         input : a, b, c they are int 
         return : sum_of_age also int"""

    def fix_age(age):
        """This func it take the age and if age == one of this numbers[13, 14, 17, 18, 19] the function return age = 0
            age = int(num)
            return : int or 0 """
        if (age == 15) or (age == 16) :
            return age
        else:
            for i in range(12, 20):
                if age == i :
                    age = 0
        return age
    
    a_new = fix_age(a)
    b_new = fix_age(b)
    c_new = fix_age(c)
    
    sum_age = a_new + b_new + c_new
    return sum_age