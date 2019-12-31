def sequence_del(my_str):
    """This func delete all the letter that excist tow or more times
       :param my_str : my_str value
       :type my_str : structure
       :return : func will return structure with letter in one time
       :rtype : structure
       """
    new = ''
    l = len(my_str)
    for i in range(l -1):
        # for j in range(1,len(my_str)):
            if my_str[i] == my_str[i+1]:
                continue
            new += my_str[i]
    new += my_str[i]
    print(new)

def main():
    sequence_del("ppyyyyythhhhhooonnnnn")
    sequence_del("SSSSsssshhhh")
    sequence_del("Heeyyy   yyouuuu!!!") 

if __name__ == "__main__":
    main()