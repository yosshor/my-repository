input_tmp = input("insert the temperature you would like to convert :")
tmp = int(input_tmp[0:2])
f_or_c = input_tmp[2]

print(tmp)
print(f_or_c)

if (f_or_c == 'F') or (f_or_c == 'f'):
    celsius = tmp * 2 + 32
    print("{}C".format(celsius))

elif (f_or_c == 'C') or (f_or_c == 'c'):
    fahrenheit = int(((9 * tmp) + (32 + 5)) / 5)
    print("{}F".format(fahrenheit))
    print("you convert the temperture from {} Celsius to {} Fahrenheit".format(tmp,fahrenheit))
