#Write a program that takes a temperature in Celsius and converts it to Fahrenheit and Kelvin, displaying all three values neatly.

# celsius = float(input("Enter the temperature in celsius: "))

# print("To Fahrenheit")
# fahrenheit = celsius * 9/5 + 32
# print(f"Celsius = {fahrenheit} Fah")

# print("To Kelvin")
# kelvin = celsius + 273
# print(f"Celsius = {kelvin} kev")


#shorter version
c = float(input("°C = "))

f = c * 9/5 + 32
k = c + 273.15

print(f"\n{c:.1f} °C  =  {f:.1f} °F  =  {k:.1f} K")

