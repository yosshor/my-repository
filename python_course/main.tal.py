import sys

def stream_input(input_path, output_file):
    with open(input_path, "r") as input_file:
        for line in input_file:
            output_file.write(line)

def print_file(file_path):
    with open(file_path, "r") as input_file:
        for line in input_file:
            print(line)

def main():
    # read parameters
    output_path = sys.argv[3]
    input_paths = sys.argv[1:3]

    with open(output_path, "w") as output_file:
        # for each input file, stream it to output file
        for input_path in input_paths:
            stream_input(input_path, output_file)

    # print the output file just to see it's ok
    print_file(output_path)

if __name__ == '__main__':
    main()