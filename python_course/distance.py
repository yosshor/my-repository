def distance(num1, num2, num3):
    if (((num2 == num1 + 1) or (num3 == num1 + 1)) and ((num2 >= num1 + 2) or (num3 >= num1 + 2))):
        return True
    return False
    
def right_distance(num1, num2, num3):
    if (((num2 == num1 + 1) or (num3 == num1 + 1)) and (((num2 > num1 + 2) and (num2 > num3 + 2))  or ((num3 > num1 + 2) and (num3 > num2 + 2)))):
        return True
    return False