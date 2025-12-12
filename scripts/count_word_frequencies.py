import re
from collections import defaultdict

def count_word_frequencies(sentence):
    """
    Count the frequency of each word in a sentence, ignoring capitalization and punctuation.
    Args:
        sentence (str): The input sentence.
    Returns:
        dict: A dictionary where keys are words and values are their respective frequencies.
    """
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    
    # Remove punctuation using regex
    sentence = re.sub(r'[^\w\s]', '', sentence)
    
    # Split the sentence into words
    words = sentence.split()
    
    # Initialize a default dictionary to store word frequencies
    word_frequencies = defaultdict(int)
    
    # Count the frequency of each word
    for word in words:
        word_frequencies[word] += 1
    
    return dict(word_frequencies)

# Example usage
if __name__ == "__main__":
    print(count_word_frequencies('Hello world'))  # {'hello': 1, 'world': 1}
    print(count_word_frequencies('Hello, hello world!'))  # {'hello': 2, 'world': 1}
    print(count_word_frequencies('A quick brown fox jumps over the lazy dog.'))  # {'a': 1, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog': 1}
    print(count_word_frequencies(''))  # {}