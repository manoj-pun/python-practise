#Write a program that takes a sentence and prints each word reversed but keeps the word order intact, then
#also prints the entire sentence reversed word-by-word.

def reverse_sentence(sentence):
    words = sentence.split()

    # Reverse each word but keep order
    reversed_each_word = []
    for word in words:
        reversed_each_word.append(word[::-1])

    print("Each word reversed:")
    print(" ".join(reversed_each_word))

    # Reverse word order
    reversed_word_order = words[::-1]

    print("\nSentence reversed word-by-word:")
    print(" ".join(reversed_word_order))


# Example
text = input("Enter a sentence: ")
reverse_sentence(text)