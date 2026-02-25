#Write a program using nested for loops to print a diamond pattern of stars of height n.

num = int(input("Enter the number (height of diamond): "))

# Upper half (including middle row)
for i in range(num):
    # spaces before stars
    for j in range(num - i - 1):
        print(" ", end=" ")
    
    # stars
    for j in range(2 * i + 1):
        print("*", end=" ")
    
    print()  # new line after each row

# Lower half (excluding the middle row)
for i in range(num - 2, -1, -1):
    # spaces before stars
    for j in range(num - i - 1):
        print(" ", end=" ")
    
    # stars
    for j in range(2 * i + 1):
        print("*", end=" ")
    
    print()  # new line