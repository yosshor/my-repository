def mult_tuple(tuple1, tuple2):
    """ the func run on the tuples and give you new tuple that is all combinations from two tuple.
        :param tuple1 : tuple1 value
        :param tuple2 : tuple2 value
        :type tuple1 : tuple
        :type tuple2 : tuple
        :return : the func return new tuple which include all the combinations from two tuples that func get.
        :rtype : tuple
        """ 
    new = []
    for i in range(len(tuple1)):
        for j in range(len(tuple2)):
            new.append(tuple((tuple1[i], tuple2[j])))
            new.append(tuple((tuple2[j], tuple1[i])))
    print(new)



def main():
    first_tuple = (1, 2, 3) 
    second_tuple = (4, 5, 6) 
    mult_tuple(first_tuple, second_tuple) 

if __name__ == "__main__":
    main()