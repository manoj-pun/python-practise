# Important Rule

# If:
# step is positive → start must be smaller than stop
# step is negative → start must be bigger than stop



#Right angle triangle

# for i in range(5):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()



#Inverter Right Angle Triangle

# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()



#Left-Aligned Triangle

# for i in range(5):
#     for j in range(5-i-1):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()


#Pyramid
# n = int(input("Enter n: "))

# for i in range(n):
#     for j in range(n - i - 1):
#         print(" ", end=" ")
#     for j in range(2 * i + 1):
#         print("*", end=" ")
#     print()


#Inverted Pyramid

# for i in range(6-1,-1,-1):
#     for j in range(6-i-1):
#         print(" ", end=" ")
#     for j in range(2*i+1):
#         print("*", end=" ")
    
#     print()


#Hollow Square

# n = int(input("Enter n: "))

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

#Bonus: Even cleaner version (many people prefer this)
# n = int(input("Enter n: "))

# for i in range(n):
#     for j in range(n):
#         if i in (0, n-1) or j in (0, n-1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


#Hollow Pyramid
n = int(input("Enter n: "))

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
