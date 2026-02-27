# palindrome for number
# def is_palindrome(num):
#     temp = num
#     reverse = 0

#     while temp > 0:
#         digit = temp % 10
#         reverse = reverse * 10 + digit
#         temp //= 10

#     return num == reverse


# num = int(input("Enter the number: "))

# if is_palindrome(num):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#Write a function is_palindrome(s) that returns True if a string is a palindrome without using slicing.
def is_palindrome(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

    return True


text = input("Enter text: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")



#with slicing
def is_palindrome(text):
    return text == text[::-1]

text = input("Enter text: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")




