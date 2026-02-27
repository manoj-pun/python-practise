# A recursive function is:
# A function that calls itself.
# Instead of using a loop, the function repeats its work by calling itself.

# def factorial(n):
#     if n == 1:          # Base case
#         return 1
#     else:
#         return n * factorial(n - 1)   # Recursive call


# print(factorial(5))


#Write a recursive function power(base, exp) that computes base^exp without using the ** operator.

def power(base, exp):
    if exp == 0:          # Base case
        return 1
    else:
        return base * power(base, exp - 1)   # Recursive call


print(power(2, 4))   # 16