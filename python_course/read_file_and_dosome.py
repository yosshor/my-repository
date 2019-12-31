
def sorting(filename):
    """This func sort the file and return the file sorted"""
    word = []
    with open(filename) as file:
        for line in file:
            word += line.split()
        return ' '.join(sorted(word))
       

def rev(filename):
    """This func take the file and return it in reverse"""
    word = []
    with open(filename) as file:
        for line in file:
            for i in line:
                if i in word:
                    continue
                word += line[::-1]
        sa = ''.join(word)
        print(set(sa))

def last(filename):
    """This func take the file read it, and you need to insert num and
       the func will return the file only with this num line"""
    word = []
    which = int(input("enter a num :"))
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
       
        for i in lines[which:]:
            print(i)
        

your_input = input("enter your path to the file.txt directory : ")
task = input("enter your task (your options is sort, rev, last) : ")

if task == str('sort'):
    r = sorting(your_input)
    print(r)
if task == 'rev':
    rev(your_input)

if task == 'last':
    last(your_input)

