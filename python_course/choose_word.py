def convert(string): 
    li = list(string.split(" ")) 
    return li 


def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist


def choose_word(file_path, index):
    word = []
    index_word = ''
    with open(file_path) as file:
        for line in file:
            word += line.split()
    new = ' '.join(unique_list(word))
    list_sent = convert(new)
    
    for i in range(1,len(list_sent) + 1):
        index %= len(list_sent)
        if i == index:
            index_word = list_sent[i - 1]
    print(len(list_sent), index_word)
    return (len(list_sent), index_word)

def main():
    file_path  = str(input("enter your file path : "))
    print(file_path)
    index = int(input('insert your index : '))
    choose_word(file_path, index)
    
    
if __name__ == "__main__":
    main()
    