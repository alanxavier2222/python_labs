def convert_temperature(temp, scale):
    if scale == 'C':
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
        return fahrenheit, kelvin
    elif scale == 'F':
        celsius = (temp - 32) * 5/9
        kelvin = (temp - 32) * 5/9 + 273.15
        return celsius, kelvin
    elif scale == 'K':
        celsius = temp - 273.15
        fahrenheit = (temp - 273.15) * 9/5 + 32
        return celsius, fahrenheit
    else:
        return None

temp = float(input("Enter the temperature value: "))
scale = input("Enter the scale (C, F, K): ").upper()

result = convert_temperature(temp, scale)
if result:
    print(f"Converted temperatures: {result}")
else:
    print("Invalid scale. Please enter C, F, or K.")
