
def who_is_missing(file_name):
    """This function look inside the file and check which num is missing
    and he is not in the file, and he write it to onther file and return it to you"""

    num = []
    w = []
    with open(file_name, 'r') as file:
        num += file.read().split(',')
        new_num = list(map(int, num))
        new_num.sort()
        for i in range(1, new_num[-1]):
            if i not in new_num:
                w.append(i)
    

    new_file = r'C:\src\first\yo.txt'
    with open(new_file, 'w') as f:
        f.write(str(w))
    with open(new_file,'r') as t:
        for i in t:
            print(i)
#    read = f.read()
#    print(read)
    
    f.close()
    
    
    
who_is_missing(r'C:\src\first\copy.txt')

