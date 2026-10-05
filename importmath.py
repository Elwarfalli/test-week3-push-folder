distance = float(input("Enter distance traveled (meters): "))
time = float(input("Enter travel time (seconds): "))

speed = distance / time

print("Conveyor Speed:", speed, "m/s")


price = float(input("Enter component price: "))
quantity = int(input("Enter quantity: "))
tax_rate = float(input("Enter tax rate (%): "))

subtotal = price * quantity
tax = subtotal * tax_rate / 100
total = subtotal + tax

print("Subtotal:", subtotal)
print("Tax:", tax)
print("Total Cost:", total)



fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9

print("Temperature in Celsius:", celsius)

"""import math

print("Some items inside the math library:")
print(dir(math))

import math

number = float(input("Enter a number: "))

print("Square root:", math.sqrt(number))
print("Power of 2:", math.pow(number, 2))
print("Ceiling:", math.ceil(number))
print("Floor:", math.floor(number))"""

import math

print(help(math.log))