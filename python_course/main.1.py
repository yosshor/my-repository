import sys

out_file = open(sys.argv[3], "w")

first_file = open(sys.argv[1], "r")
for line in first_file:
    out_file.write(line)
first_file.close()

second_file = open(sys.argv[2], "r")
for line1 in second_file:
    out_file.write(line1)
second_file.close()

out_file.close()
read_out_file = open(sys.argv[3], "r")
for lines_second_file in read_out_file:
    print(lines_second_file)