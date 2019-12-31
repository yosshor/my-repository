my_dict = {'first_name ': 'Mariah', 'last_name' : 'Carey', 'birth_date' : '27.03.1970',
           'hobbies' : ['Sing', 'Compose', 'act']}

def dict1():
    num1 = int(input('enter a num between 1 - 7 : '))
    x = ()
    new =()

    if num1 == 1:
        print(my_dict['last_name'])

    if num1 is 2:
        x = my_dict['birth_date'].split(".")
        print('Mariah was born on {} in a year'.format(x[1]))

    if num1 == 3:
        print('Mariah has {} hobbies '.format(len(my_dict['hobbies'])))

    if num1 == 4:
        print("the last of hobbies's Mariah is {} ".format(my_dict['hobbies'][2]))

    if num1 == 5:
        my_dict['hobbies'].append('Cooking')
        print(my_dict['hobbies'])

    if num1 == 6:
        x = my_dict['birth_date'].split(".")
        for i in range(len(x)):
            new += (x[i],)
        print(new)
        print(type(new))

    if num1 == 7:
        my_dict['age'] = '49'
        for key in my_dict.items():
            print(key)


def main():
    dict1()

if __name__ == "__main__":
    main()