#Write a function word_frequency(text) that takes a paragraph and returns a dictionary of each word and its
#count, case-insensitively.

def word_frequency(text):
    # Convert text to lowercase to make it case-insensitive
    text = text.lower()
    
    # Split text into words (basic splitting by whitespace)
    words = text.split()
    
    # Initialize an empty dictionary
    freq = {}
    
    # Count each word
    for word in words:
        # Remove punctuation from start and end of word
        word = word.strip(".,!?;:\"'()[]{}")
        if word:  # make sure word is not empty after stripping
            freq[word] = freq.get(word, 0) + 1
    
    return freq

# Example usage:
paragraph = "Hello world! Hello Python. Python is great, and Python is fun."
print(word_frequency(paragraph))
