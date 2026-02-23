#Create a program that swaps two variables without using a third variable, then prints both before and after.
 
a = input("Enter the first value: ")
b = input("Enter the second value: ")

print("Befor swapping")
print(f"a = {a}")
print(f"b = {b}")

a,b = b,a

print("After swapping")
print(f"a = {a}")
print(f"b = {b}")

