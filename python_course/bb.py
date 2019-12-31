input_tmp = input("insert the temperature you would like to convert :")
tmp = input_tmp[0:2]
f_or_c = input_tmp[2]

print(tmp)
print(f_or_c)

if (f_or_c == 'F') or (f_or_c == 'f'):
    celsius = tmp * 2 + 32
    print("{}C".format(celsius))
   # return celsius

elif (f_or_c == 'C') or (f_or_c == 'c'):
    fahrenheit = (9 * tmp + (32 + 5)) / 5
    print("{}F".format(fahrenheit))





















""" pigs = 3
num_input = input("enter three digits (each digit for one pig) : ")
sum_input = int(num_input[0]) + int(num_input[1]) + int(num_input[2])
print(sum_input)

each_pig_get = sum_input // pigs
print(each_pig_get)
print(sum_input % pigs)
check = sum_input % pigs

print(check == 0)



 input_str = input("enter your string: ")
check_the_len = len(input_str) // 2
new_str = input_str[0:check_the_len].lower() + input_str[check_the_len:].upper()
print(new_str)


enter_str = input("enter some string :")
enter_str = enter_str.replace(" ", "") 
enter_str = enter_str.lower()

len_input = len(enter_str) // 2

if enter_str[0:len_input] == enter_str[-1:-(len_input + 1):-1]:
    print("OK")
    print(enter_str[0:len_input])   
    print(enter_str[-1:-(len_input + 1):-1])
else:
    print("NOT")
    print(enter_str[0:len_input])   
    print(enter_str[-1:-(len_input + 1):-1])
    print(len_input) 
"""

