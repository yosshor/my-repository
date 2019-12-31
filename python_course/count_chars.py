def count_chars(my_str):
    new = {}
    new_my_str = my_str.replace(" ", "")
    for i in range(len(new_my_str)):
        new[new_my_str[i]] = new_my_str.count(new_my_str[i])
    print(new)
    print(new.keys())

def main():
    magic_str = "abra cadabra"
    count_chars(magic_str)

if __name__ == "__main__":
    main()