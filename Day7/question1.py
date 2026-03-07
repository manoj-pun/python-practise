#Write a function caesar_cipher(text, shift) that encrypts and decrypts a string using the Caesar cipher
#technique.

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine ASCII starting point
            start = ord('A') if char.isupper() else ord('a')

            # Shift character
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char

    return result

message = "Hello World"

encrypted = caesar_cipher(message, 3)
print("Encrypted:", encrypted)

decrypted = caesar_cipher(encrypted, -3)
print("Decrypted:", decrypted)