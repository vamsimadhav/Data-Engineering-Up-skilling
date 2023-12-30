def convert_temperature(temp, direction):
    if direction == 'F_to_C':
        convert_temp = (temp - 32) * 5 / 9
        return convert_temp
    elif direction == 'C_to_F':
        convert_temp = (temp * 9 / 5) + 32
        return convert_temp
    else:
        return 'Invalid Conversion'


temp = int(input("Enter the temperature value: "))

print("Please select your option \n"
      "1) F_to_C => Fahrenheit to Celsius \n"
      "2) C_to_F => Celsius to Fahrenheit \n"
      )

option = int(input("Enter your selection: "))

selection = 'invalid'

if option == 1:
    selection = 'F_to_C'
elif option == 2:
    selection = 'C_to_F'

print(convert_temperature(temp,selection))


