#Print the Fibonacci sequence up to n terms using a while loop, where n is taken from the user.

num = int(input("Enter number of terms: "))

if num <= 0:
    print("Please enter a positive integer")
else:
    a, b = 0, 1
    count = 0
    
    print("Fibonacci sequence:")
    
    while count < num:
        print(a, end=" ")
        a, b = b, a + b      
        count += 1
        
    print()



# x = 0

# while x < 3:
#     x += 1

# print(x)
