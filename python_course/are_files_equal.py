# def are_files_equal(file1, file2):
#     for line1 in file1.readline():
#         for line2 in file2.readline():
#             if line1 == line2:
#                 return True
#             return False 

def are_files_equal(file1, file2):
    """the function check if the files are equal"""
    ww = open(file1, 'r')
    ee = open(file2, 'r')
    for line in ww:
        for line1 in ee:
            if line == line1:
                print(True)
                return True
            print(False)
            return False



are_files_equal(r"C:\src\first\yoss1.txt", r"C:\src\first\yoss2.txt")
