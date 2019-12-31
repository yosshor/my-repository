def copy_file_content(source, destination):
    """This function take the information from source file and copy that to destination file"""
    data = ''
    e = ''
    
    with open(source, 'r') as file:
        for line in file:
            data += line
    
    t = open(destination, 'w')
    t.write(data)
    t.close()

    with open(destination, 'r') as file2:
        for line1 in file2:
            print(line1)
            # e += line1
    # print(e)



copy_file_content(r'C:\src\first\copy.txt', r'C:\src\first\destination.txt')




# 
# def copy_file_content(source, destination):
#     data = ''
#     e = ''
#     with open(source, 'r') as file:
#         for line in file:
#             data += line
#     t = open(destination, 'w')
# 
#     t.write(data)
#     # r = open(r'C:\src\first\destination.txt', 'r')
#     # for i in r.readlines():
#     #     print(i)
#     with open(destination, 'r') as file2:
#         for line1 in file2:
#             e += line1
#     print(e)
# 
# 
# 
# copy_file_content(r'C:\src\first\copy.txt', r'C:\src\first\destination.txt')
# 
# 
